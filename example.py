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