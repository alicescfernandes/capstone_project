import os
import pandas as pd
import plotly.express as px
from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.views import View


# Get the path to the xlsx directory
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
xlsx_dir = os.path.join(current_dir, 'xlsx')

import pandas as pd
from django.http import JsonResponse
from django.views import View
import os

def customer_needs_by_need(request, quarter):
    segment = request.GET.get("segment") 

    if not quarter:
        return JsonResponse({"error": "Missing 'quarter'"}, status=400)

    file_path = f"uploads/CustomerNeeds-Q{quarter}.xlsx"
    if not os.path.exists(file_path):
        return JsonResponse({"error": "File not found"}, status=404)

    try:
        df = pd.read_excel(file_path, skiprows=1)
        df.columns = ['Need', 'Costcutter', 'Innovator', 'Mercedes', 'Workhorse', 'Traveler']
    except Exception as e:
        return JsonResponse({"error": f"Error reading file: {str(e)}"}, status=500)

    available_segments = df.columns[1:].tolist()

    # Se não passar o segmento, usa o primeiro
    selected_segment = segment if segment in available_segments else available_segments[0]

    # Construir os dados do gráfico
    needs = df['Need'].fillna("").tolist()
    values = df[selected_segment].fillna(0).tolist()

    response = {
        "section": "customer-needs-by-need",
        "quarter": quarter,
        "data": {
            "id": "bar-chart",
            "x": needs,
            "y": values
        },
        "segments": available_segments
    }

    return JsonResponse(response)


def customer_needs_by_segment(request, quarter):
    need_param = request.GET.get("need") 

    if not quarter:
        return JsonResponse({"error": "Missing 'quarter'"}, status=400)

    file_path = f"uploads/CustomerNeeds-Q{quarter}.xlsx"
    if not os.path.exists(file_path):
        return JsonResponse({"error": "File not found"}, status=404)

    try:
        df = pd.read_excel(file_path, skiprows=1)
        df.columns = ['Need', 'Costcutter', 'Innovator', 'Mercedes', 'Workhorse', 'Traveler']
    except Exception as e:
        return JsonResponse({"error": f"Error reading file: {str(e)}"}, status=500)

    # Lista completa de needs disponíveis
    available_needs = df['Need'].dropna().tolist()

    if not available_needs:
        return JsonResponse({"error": "No needs found in file"}, status=400)

    # Usar a necessidade passada ou a primeira como predefinida
    selected_need = need_param if need_param in available_needs else available_needs[0]

    row = df[df['Need'] == selected_need]
    if row.empty:
        return JsonResponse({"error": "Selected need not found"}, status=404)

    values_dict = row.iloc[0].drop('Need').to_dict()

    response = {
        "section": "customer-needs-by-segment",
        "quarter": quarter,
        "data": {
            "id": "pie-chart",
            "labels": list(values_dict.keys()),
            "values": list(values_dict.values())
        },
        "needs": available_needs
    }

    return JsonResponse(response)


def charts(request, section, quarter):
    try:
        if section == 'customer-needs-by-segment':
            return customer_needs_by_segment(request, quarter)
        if section == 'customer-needs-by-need':
            return customer_needs_by_need(request, quarter)
        return JsonResponse({"section": section, "quarter": quarter, "data": []})
    except Exception as e:
        raise Http404(f"Erro ao carregar dados: {e}")


def home(request):
    
    return render(request, 'pages/home.html', {'sections': [], 'error': None })
    
