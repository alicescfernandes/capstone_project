import os
import pandas as pd
import plotly.express as px
from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.views import View


# Get the path to the xlsx directory
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
xlsx_dir = os.path.join(current_dir, 'xlsx')

def open_file(file_path):
    df = pd.read_excel(file_path)
    df.columns = df.iloc[0]  # Primeira linha contém os nomes corretos
    df = df.drop(index=0).reset_index(drop=True)

    df = df[~df[df.columns[0]].astype(str).str.lower().str.contains("end of worksheet", na=False)]
    df = df[df[df.columns[0]].notna() & (df[df.columns[0]] != "")]
    return df

def use_pattern_by_segment(request, quarter):
    segment = request.GET.get("segment")

    if not quarter:
        return JsonResponse({"error": "Missing 'quarter'"}, status=400)

    file_path = f"uploads/UsePattern-Q{quarter}.xlsx"
    if not os.path.exists(file_path):
        return JsonResponse({"error": "File not found"}, status=404)

    try:
        df = open_file(file_path)

        application_col = df.columns[0]
        segment_cols = df.columns[1:]

        df[segment_cols] = df[segment_cols].apply(pd.to_numeric, errors='coerce')

        available_segments = segment_cols.tolist()
        selected_segment = segment if segment in available_segments else available_segments[0]

        applications = df[application_col].fillna("").tolist()
        values = df[selected_segment].fillna(0).tolist()

    except Exception as e:
        return JsonResponse({"error": f"Error reading file: {str(e)}"}, status=500)

    response = {
        "section": "use-pattern-by-segment",
        "quarter": quarter,
        "data": {
            "id": "bar-chart",
            "x": applications,
            "y": values
        },
        "segments": available_segments
    }

    return JsonResponse(response)

def use_pattern_by_application(request, quarter):
    if not quarter:
        return JsonResponse({"error": "Missing 'quarter'"}, status=400)

    file_path = f"uploads/UsePattern-Q{quarter}.xlsx"
    if not os.path.exists(file_path):
        return JsonResponse({"error": "File not found"}, status=404)

    try:
        df = open_file(file_path)

        # Nome da coluna com as aplicações
        application_col = df.columns[0]
        segment_cols = df.columns[1:]

        df[segment_cols] = df[segment_cols].apply(pd.to_numeric, errors='coerce')

        applications = df[application_col].fillna("").tolist()
        segments = segment_cols.tolist()
        stacked_values = {segment: df[segment].fillna(0).tolist() for segment in segments}

    except Exception as e:
        return JsonResponse({"error": f"Error reading file: {str(e)}"}, status=500)

    response = {
        "section": "use-pattern-by-application",
        "quarter": quarter,
        "data": {
            "id": "stacked-bar-chart",
            "x": applications,
            "series": [{"name": seg, "data": stacked_values[seg]} for seg in segments]
        },
        "segments": segments
    }

    return JsonResponse(response)

def customer_needs_by_need(request, quarter):
    segment = request.GET.get("segment") 

    if not quarter:
        return JsonResponse({"error": "Missing 'quarter'"}, status=400)

    file_path = f"uploads/CustomerNeeds-Q{quarter}.xlsx"
    if not os.path.exists(file_path):
        return JsonResponse({"error": "File not found"}, status=404)

    try:
        df = open_file(file_path)
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
        df = open_file(file_path)
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

def use_pattern_grouped_bar(request, quarter):
    if not quarter:
        return JsonResponse({"error": "Missing 'quarter'"}, status=400)

    file_path = f"uploads/UsePattern-Q{quarter}.xlsx"
    if not os.path.exists(file_path):
        return JsonResponse({"error": "File not found"}, status=404)

    try:
        df = open_file(file_path)

        application_col = df.columns[0]
        segment_cols = df.columns[1:]

        df[segment_cols] = df[segment_cols].apply(pd.to_numeric, errors='coerce')

        applications = df[application_col].fillna("").tolist()
        segments = segment_cols.tolist()
        grouped_values = {segment: df[segment].fillna(0).tolist() for segment in segments}

    except Exception as e:
        return JsonResponse({"error": f"Error reading file: {str(e)}"}, status=500)

    response = {
        "section": "use-pattern-by-application",
        "quarter": quarter,
        "data": {
            "id": "grouped-bar-chart",
            "x": applications,
            "series": [
                {"name": seg, "data": grouped_values[seg]} for seg in segments
            ]
        },
        "segments": segments
    }

    return JsonResponse(response)

import os
import pandas as pd
from django.http import JsonResponse

def market_demand_pie_by_segment(request, quarter):
    segment = request.GET.get("segment")
    facet = request.GET.get("facet")

    if not quarter:
        return JsonResponse({"error": "Missing 'quarter'"}, status=400)

    if not facet:
        return JsonResponse({"error": "Missing 'facet'"}, status=400)

    if facet not in ["market_demand", "market_share"]:
        return JsonResponse({"error": "Invalid 'facet'"}, status=400)

    sheet_name = "Market Demand" if facet == "market_demand" else "Market Share"

    file_path = f"uploads/MarketShare-Q{quarter}.xlsx"

    print(sheet_name)
    if not os.path.exists(file_path):
        return JsonResponse({"error": "File not found"}, status=404)

    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        df.columns = df.iloc[0]
        df = df.drop(index=0).reset_index(drop=True)

        # Remover "Total Demand" e linhas inválidas
        df = df.drop(columns=["Total Demand"], errors="ignore")
        df = df[~df["Company"].astype(str).str.lower().str.contains("total|end of worksheet", na=False)]

        segments = df.columns[1:]
        selected = segment if segment in segments else segments[0]

        labels = df["Company"].fillna("").tolist()
        values = pd.to_numeric(df[selected], errors="coerce").fillna(0).tolist()

    except Exception as e:
        return JsonResponse({"error": f"Error reading file: {str(e)}"}, status=500)

    return JsonResponse({
        "section": "market-demand-pie-by-segment",
        "quarter": quarter,
        "data": {
            "id": "pie-chart-by-segment",
            "labels": labels,
            "values": values
        },
        "segments": segments.tolist()
    })


def charts(request, section, quarter):
    try:
        if section == 'customer-needs-by-segment':
            return customer_needs_by_segment(request, quarter)
        if section == 'customer-needs-by-need':
            return customer_needs_by_need(request, quarter)
        if section == 'use-pattern-by-application':
            return use_pattern_by_application(request, quarter)
        if section == 'use-pattern-by-segment':
            return use_pattern_by_segment(request, quarter)
        if section == 'use-pattern-grouped-bar':
            return use_pattern_grouped_bar(request, quarter)
        if section == 'market-demand-pie-by-segment':
            return market_demand_pie_by_segment(request, quarter)
        return JsonResponse({"section": section, "quarter": quarter, "data": []})
    except Exception as e:
        raise Http404(f"Erro ao carregar dados: {e}")


def home(request):
    
    return render(request, 'pages/home.html', {'sections': [], 'error': None })
    
