import pandas as pd

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from pages.models import Quarter
from .models import Quarter
from .utils.chart_classification import CHART_CLASSIFICATION
from .utils.api import  get_quarter_navigation_object, get_request_params, return_empty_response, get_active_csv_for_slug
from .utils.charts import get_simple_chart, get_double_chart, get_waterfall_chart, get_group_chart, get_sankey_chart, get_table_chart

class QuarterListAPIView(APIView):
    def get(self, request):
        # Preparar a lista de quarters
        quarters = Quarter.objects.filter(user=request.user)
        last_quarter = quarters[0]
        if not quarters:
            return Response({"error": "No quarters found"}, status=404)

        first_quarter = quarters[::-1][0]     # mais antigo

        # Obter o número do quarter pedido (ou usar o último por defeito)
        query_quarter = request.query_params.get("q", last_quarter.number)

        try:
            quarter = quarters.get(number=int(query_quarter))
        except Quarter.DoesNotExist:
            return Response({"error": "Quarter not found"}, status=404)

        # Resposta JSON personalizada
        return Response({
            "number": quarter.number,
            "uuid": str(quarter.uuid),
            "isFirst": quarter.number == first_quarter.number,
            "isLast": quarter.number == last_quarter.number,
            "float_precision": quarter.float_precision
        })

# http://localhost:8000/api/chart/?slug=customer-needs-and-wants&q=1
# http://localhost:8000/api/chart/?slug=competitors-prices-apac&q=1
class ChartDataAPIView(APIView):
    def get(self, request):
        slug, quarter_number, filter = get_request_params(request)
        
        if not slug:
            return Response(
                {"error": "Missing required 'slug' query parameter."},
                status=status.HTTP_400_BAD_REQUEST
            )

        chart_meta = CHART_CLASSIFICATION.get(slug)
        
        if not chart_meta:
            return Response(
                {"error": f"No chart classification found for slug '{slug}'."},
                status=status.HTTP_404_NOT_FOUND
            )

        type = chart_meta["type"]

        quarter_data = get_quarter_navigation_object(quarter_number, slug, request.user) 
        csv_data = get_active_csv_for_slug(quarter_number, slug, request.user)

        try:
            df = pd.DataFrame(csv_data.data)
            df = df[csv_data.column_order] 

            if(type == "simple"):
                chart_response = get_simple_chart(df, chart_meta,csv_data.sheet_name_pretty, filter)
                return Response(quarter_data | chart_response)
        
            if(type=="double"):
                chart_response = get_double_chart(df, chart_meta,csv_data.sheet_name_pretty, filter)
                return Response(quarter_data | chart_response)
            
            if(type=="balance_sheet"):
                chart_response = get_waterfall_chart(df, chart_meta,csv_data.sheet_name_pretty, filter)
                return Response(quarter_data | chart_response)
            
            if(type=="grouped"):
                chart_response = get_group_chart(df, chart_meta,csv_data.sheet_name_pretty, filter)
                return Response(quarter_data | chart_response)
            
            if(type=="sankey"):
                chart_response = get_sankey_chart(df, chart_meta,csv_data.sheet_name_pretty, filter)
                return Response(quarter_data | chart_response)
        
            if(type =="table"):
                chart_response = get_table_chart(df, chart_meta,csv_data.sheet_name_pretty, filter)
                return Response(quarter_data | chart_response)    
            
        except Exception as e:
            empty_response = return_empty_response(quarter_number, slug, e, csv_data.sheet_name_pretty)
            return Response(quarter_data | empty_response )