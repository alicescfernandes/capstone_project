from ..models import Quarter, CSVFile
from django.shortcuts import get_object_or_404

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
        "quarter":{
            'current': curr_q.number,
            'prev': prev_q.number if prev_q else None,
            'next': next_q.number if next_q else None,
        }
    }


def get_request_params(request):
    quarters = Quarter.objects.all()
    last_quarter = quarters[0]

    slug = request.query_params.get('slug')
    quarter_number = request.query_params.get('q', last_quarter.number)
    filter = request.query_params.get('opt')  # opcional
    
    return slug,quarter_number,filter


def return_empty_response(quarter_number, slug,error,sheet_name ):
    return {
        "error": f"Error reading file: {str(error)}",
        'chart_config':{
            "traces":[],
            "layout":{}
        },
        'title': sheet_name,
        "options": [],
        'selected_option': None
    }


def get_active_csv_for_slug(quarter_number, slug):
    curr_q = get_object_or_404(Quarter, number=quarter_number)
    csv_file = get_object_or_404(
        CSVFile,
        sheet_name_slug=slug,
        quarter_uuid=curr_q.uuid,
        is_current=True)
    return csv_file