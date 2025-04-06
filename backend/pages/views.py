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
from django.db.models import Max
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Quarter
from .forms import QuarterForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Quarter
from .forms import QuarterForm

# Get the path to the xlsx directory
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
xlsx_dir = os.path.join(current_dir, 'xlsx')

def home(request):
    # Prepare default case
    quarters = Quarter.objects.all()
    if(len(quarters) <= 0):
        return render(request, 'pages/home.html', {
        "app_context":{
            "qn":None,
            "quuid":None,            
        },
        "empty":True,
        "chart_slugs": []
    })
    
    last_quarter = quarters[0]
    first_quarter = quarters[::-1][0]
        
    # Use query params here with default values
    query_quarter = request.GET.get("q",last_quarter.number)
    quarter = Quarter.objects.get(number=int(query_quarter))

    unique_slugs = list(CSVFile.objects.values_list('sheet_name_slug', flat=True).distinct())    
    print(unique_slugs)
    
    latest_csvs = (
        CSVFile.objects
        .select_related('quarter_file__quarter')
        .order_by('sheet_name_slug', '-quarter_file__quarter__number')
        )
    
    # Filtrar para manter apenas o primeiro CSV por slug
    seen_slugs = set()
    chart_slugs = []

    for csv in latest_csvs:
        slug = csv.sheet_name_slug
        if slug not in seen_slugs:
            seen_slugs.add(slug)

            chart_slugs.append({
                "slug": slug,
                "quarter_number": csv.quarter_file.quarter.number,
            })
            

    return render(request, 'pages/home.html', {
        "app_context":{
            "qn":quarter.number,
            "quuid":quarter.uuid,            
        },
        "chart_slugs": chart_slugs
    })

def manage_quarters(request):
    quarters = Quarter.objects.all()
    form = QuarterForm()

    if request.method == 'POST':
        form = QuarterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_quarters')

    return render(request, 'pages/manage_quarters.html', {
        'form': form,
        'quarters': quarters,
    })

def delete_quarter(request, uuid):
    quarter = get_object_or_404(Quarter, uuid=uuid)
    quarter.delete()
    return redirect('manage_quarters')


def delete_file(request, uuid):
    quarter = get_object_or_404(ExcellFile, uuid=uuid)
    quarter.delete()
    return redirect('manage_quarters')


def edit_quarter(request, uuid):
    quarter = get_object_or_404(Quarter, uuid=uuid)

    if request.method == 'POST':
        # Atualizar número do quarter
        new_number = request.POST.get('number')
        if new_number:
            quarter.number = new_number
            quarter.save()

        # Upload de múltiplos ficheiros
        files = request.FILES.getlist('files')
        print("files", files)
        for f in files:
            excell_file = ExcellFile.objects.create(
                quarter=quarter,
                file=f
            )

    return redirect('manage_quarters')