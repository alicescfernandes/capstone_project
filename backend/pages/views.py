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

# Get the path to the xlsx directory
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
xlsx_dir = os.path.join(current_dir, 'xlsx')

def home(request):
    # Prepare default case
    quarters = Quarter.objects.all()
    last_quarter = quarters[0]
    first_quarter = quarters[::-1][0]
        
    # Use query params here with default values
    query_quarter = request.GET.get("q",last_quarter.number)
    quarter = Quarter.objects.get(number=int(query_quarter))

    unique_slugs = list(CSVFile.objects.values_list('sheet_name_slug', flat=True).distinct())    
    print(unique_slugs)
    
    return render(request, 'pages/home.html', {
        "app_context":{
            "qn":quarter.number,
            "quuid":quarter.uuid,            
        },
        "chart_slugs": unique_slugs
    })
