import os
import pandas as pd
import plotly.express as px
from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.views import View
from pages.models import Quarter
import os
import pandas as pd
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Quarter, ExcellFile, CSVFile
from .serializers import QuarterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CSVFile
from django.shortcuts import get_object_or_404
import pandas as pd

# Get the path to the xlsx directory
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
xlsx_dir = os.path.join(current_dir, 'xlsx')

class QuarterListAPIView(APIView):
    def get(self, request):
        # Preparar a lista de quarters
        quarters = Quarter.objects.all()
        if not quarters:
            return Response({"error": "No quarters found"}, status=404)

        last_quarter = quarters[0]            # mais recente
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

# http://localhost:8000/api/chart/?slug=customer_needs_and_wants&quarter=1eac6e9c-f4a3-4d28-b9e5-0837b2e2c0e3
class ChartDataAPIView(APIView):
    def get(self, request, format=None):
        slug = request.query_params.get('slug')
        quarter_uuid = request.query_params.get('quarter')

        if not slug or not quarter_uuid:
            return Response(
                {"error": "Both 'slug' and 'quarter' query parameters are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        csv_file = get_object_or_404(
            CSVFile,
            sheet_name_slug='customer_needs_and_wants',
            quarter_uuid='1eac6e9c-f4a3-4d28-b9e5-0837b2e2c0e3'
        )
        

        try:
            df = pd.read_csv(csv_file.csv_path)
        except Exception as e:
            return Response(
                {"error": f"Erro ao ler o ficheiro CSV: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # Limita a 100 linhas, por exemplo
        first_col_name = df.columns[0]
        print("hello")
        first_col_data = df[first_col_name].to_string()
        
        print("data 2:" + first_col_data)
        return Response({
            "slug2": slug,
            "quarter_uuid": quarter_uuid,
            "data": "data"
        })