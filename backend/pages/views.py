import os
import openpyxl
from django.core.exceptions import ValidationError
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Quarter, ExcelFile, CSVData
from .utils.chart_classification import CHART_CLASSIFICATION_KEYS
from django.utils.text import slugify


# Get the path to the xlsx directory
current_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
xlsx_dir = os.path.join(current_dir, 'xlsx')

def is_valid_xlsx(file):
    if not file.name.endswith('.xlsx'):
        raise ValidationError("Extensão inválida: apenas ficheiros .xlsx são permitidos.")
    
    if file.content_type != 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        raise ValidationError("Tipo MIME inválido para ficheiro .xlsx.")

    try:
        file.seek(0)
        openpyxl.load_workbook(file)
        file.seek(0)
    except Exception as e:
        raise ValidationError("Conteúdo inválido: o ficheiro não é um Excel válido.") from e
    
@login_required
def home(request):
    quarters = Quarter.objects.filter(user=request.user)

    if not quarters.exists():
        return render(request, 'pages/home.html', {
            "app_context": {
                "qn": None,
                "quuid": None,
            },
            "empty": True,
            "chart_slugs": []
        })

    latest_csvs = (
        CSVData.objects
        .filter(user=request.user, is_current=True)
        .select_related('quarter_file__quarter')
        .order_by('sheet_name_slug', '-quarter_file__quarter__number')
    )

    seen_chart_slugs = set()
    all_charts = []
    charts_by_section = {}

    for csv in latest_csvs:
        chart_slug = csv.sheet_name_slug
        if chart_slug in seen_chart_slugs or chart_slug not in CHART_CLASSIFICATION_KEYS:
            continue

        seen_chart_slugs.add(chart_slug)

        section_title = csv.quarter_file.section_name or "All"
        section_slug = slugify(section_title)

        chart_info = {
            "slug": chart_slug,
            "title": csv.sheet_name_pretty,
            "quarter_number": csv.quarter_file.quarter.number,
        }

        if section_slug not in charts_by_section:
            charts_by_section[section_slug] = {
                "slug": section_slug,
                "title": section_title,
                "charts": []
            }

        charts_by_section[section_slug]["charts"].append(chart_info)
        all_charts.append(chart_info)

    toc_data = list(charts_by_section.values())

    if toc_data and isinstance(toc_data[0], dict):
        default_section_slug = toc_data[0].get("slug")
    else:
        default_section_slug = None

    selected_section_slug = request.GET.get("section", default_section_slug)

    selected_section = next(
        (section for section in toc_data if section["slug"] == selected_section_slug),
        None
    )

    selected_charts = selected_section["charts"] if selected_section else []
    selected_section_title = selected_section["title"] if selected_section else "Unknown"


    toc_data = list(charts_by_section.values())
    toc_data.sort(key=lambda section: section["title"].lower())

    return render(request, 'pages/home.html', {
        "toc_data": toc_data,
        "selected_section_slug": selected_section_slug,
        "selected_section_title": selected_section_title,
        "selected_charts": selected_charts,
        "empty": len(all_charts) == 0,
    })


@login_required
def manage_quarters(request):
    quarters = Quarter.objects.filter(user=request.user)
    next_q = 1
    
    if(len(quarters) > 0):
        next_q = quarters.first().number + 1

    return render(
        request,
        "pages/manage_quarters.html",
        {
            "quarters": quarters,
            "next_q": next_q
        },
    )

    return render(request, 'pages/manage_quarters.html', {
        'form': form,
        'quarters': quarters,
    })

@login_required
def delete_quarter(request, uuid):
    quarter = get_object_or_404(Quarter, uuid=uuid, user=request.user)
    quarter.delete()
    return redirect('manage_quarters')

@login_required
def delete_file(request, uuid):
    quarter = get_object_or_404(ExcelFile, uuid=uuid, user=request.user)
    quarter.delete()
    return redirect('manage_quarters')

@login_required
def edit_quarter(request, uuid=None):
    quarter = None

    if uuid is None:
        quarter = Quarter(user=request.user)
    else:
        quarter = Quarter.objects.get(uuid=uuid, user=request.user)

    if request.method == "POST":
        new_number = request.POST.get("number")

        if not new_number:
            return redirect("manage_quarters")

        if quarter:
            quarter.number = new_number
        else:
            quarter = Quarter(number=new_number, user=request.user)

        quarter.save()

        files = request.FILES.getlist('files')
        for f in files:
            try:
                is_valid_xlsx(f)
                ExcelFile.objects.create(
                    quarter=quarter,
                    file=f,
                    user=request.user
                )
            except ValidationError as e:
                print(f"Did not upload '{f.name}': {e}")
                continue

        return redirect("manage_quarters")

    return redirect("manage_quarters")

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # ou outro destino

class CustomLoginView(LoginView):
    template_name = "pages/login.html"
    redirect_authenticated_user = True 
    next_page = reverse_lazy("home") 

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'pages/register.html', {'form': form})