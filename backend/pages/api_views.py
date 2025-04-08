import os
import pandas as pd
from pages.models import Quarter
import os
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Quarter, CSVFile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CSVFile
from django.shortcuts import get_object_or_404
import pandas as pd
class QuarterListAPIView(APIView):
    def get(self, request):
        # Preparar a lista de quarters
        quarters = Quarter.objects.all()
        last_quarter = quarters[0]
        if not quarters:
            return Response({"error": "No quarters found"}, status=404)

        first_quarter = quarters[::-1][0]     # mais antigo

        # Obter o número do quarter pedido (ou usar o último por defeito)
        query_quarter = request.query_params.get("q", last_quarter.number)

        try:
            quarter = Quarter.objects.get(number=int(query_quarter))
        except Quarter.DoesNotExist:
            return Response({"error": "Quarter not found"}, status=404)

        # Resposta JSON personalizada
        return Response({
            "number": quarter.number,
            "uuid": str(quarter.uuid),
            "isFirst": quarter.number == first_quarter.number,
            "isLast": quarter.number == last_quarter.number,
        })

def get_quarter_navigation_object(quarter_number, slug):
    # Obter todos os quarter_uuids associados ao slug
    quarter_uuids = (
        CSVFile.objects
        .filter(is_current=True) 
        .filter(sheet_name_slug=slug)
        .values_list('quarter_uuid', flat=True)
        .distinct()
    )
    
    # Obter os objetos Quarter correspondentes, ordenados por número
    all_quarters = list(
        Quarter.objects
        .filter(uuid__in=quarter_uuids)
        .order_by('number')
    )

    curr_q = get_object_or_404(Quarter, number=quarter_number)

    try:
        current_index = next(i for i, q in enumerate(all_quarters) if q.pk == curr_q.pk)
    except StopIteration:
        return None  # current quarter não está na lista filtrada

    prev_q = all_quarters[current_index - 1] if current_index > 0 else None
    next_q = all_quarters[current_index + 1] if current_index < len(all_quarters) - 1 else None

    return {
        'current': curr_q.number,
        'prev': prev_q.number if prev_q else None,
        'next': next_q.number if next_q else None,
    }

# http://localhost:8000/api/chart/?slug=customer_needs_and_wants&q=1
class ChartDataAPIView(APIView):
    def get(self, request, format=None):
        quarters = Quarter.objects.all()
        last_quarter = quarters[0]            # mais recente

        slug = request.query_params.get('slug')
        quarter_number = request.query_params.get('q', last_quarter.number)
        filter = request.query_params.get('opt')  # opcional

        if not slug:
            return Response(
                {"error": "Both 'slug' query parameters are required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        curr_q = get_object_or_404(Quarter, number=quarter_number)
        
        csv_file = get_object_or_404(
            CSVFile,
            sheet_name_slug=slug,
            quarter_uuid=curr_q.uuid,
            is_current=True
        )

        file_path = csv_file.csv_path
                
        try:
            df = pd.read_csv(file_path)

            application_col = df.columns[0]
            filter_cols = df.columns[1:]

            df[filter_cols] = df[filter_cols].apply(pd.to_numeric, errors='coerce')

            available_filters = filter_cols.tolist()
            selected_filter = filter if filter in available_filters else available_filters[0]

            applications = df[application_col].fillna("").tolist()
            values = df[selected_filter].fillna(0).tolist()

        except Exception as e:
            return Response({"error": f"Error reading file: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            'quarter':get_quarter_navigation_object(quarter_number, slug),
            "data": {
                "type": "bar", #TODO: Mapping for slugs to chart types
                "x": applications,
                "y": values
            },
            'title': csv_file.sheet_name,
            "options": available_filters,
            'selected_option': selected_filter
        })