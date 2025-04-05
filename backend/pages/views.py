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
from .models import Quarter
from .serializers import QuarterSerializer

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
            "quarter": {
                "number": quarter.number,
                "uuid": str(quarter.uuid),
            },
            "isFirst": quarter.number == first_quarter.number,
            "isLast": quarter.number == last_quarter.number,
        })


def home(request):
    # Prepare default case
    quarters = Quarter.objects.all()
    last_quarter = quarters[0]
    first_quarter = quarters[::-1][0]
        
    # Use query params here with default values
    query_quarter = request.GET.get("q",last_quarter.number)
    quarter = Quarter.objects.get(number=int(query_quarter))


    return render(request, 'pages/home.html', {
        "quarter":quarter,
        "hasPrevious": quarter.number > first_quarter.number,
        "hasNext": quarter.number < last_quarter.number,
        "last":last_quarter.number,
        "first": first_quarter.number,
    })
