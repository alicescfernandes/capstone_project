from django.shortcuts import render
from .models import Chart

# Create your views here.

def home(request):
    charts = Chart.objects.filter(is_active=True)
    return render(request, 'app/home.html', {'charts': charts})

def about(request):
    return render(request, 'app/about.html')

def charts(request):
    charts = Chart.objects.filter(is_active=True)
    print("Number of charts:", charts.count())  # Debug print
    for chart in charts:
        print(f"Chart {chart.id}: {chart.title}")  # Debug print
        print(f"Config: {chart.get_chart_config()}")  # Debug print
    return render(request, 'app/charts.html', {'charts': charts})
