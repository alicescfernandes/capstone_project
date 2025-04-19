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
from .forms import QuarterForm

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
    # Prepare default case
    quarters = Quarter.objects.filter(user=request.user)
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

    quarter = quarters.get(number=int(last_quarter.number))
    
    latest_csvs = (
        CSVData.objects
        .filter(user=request.user)
        .select_related('quarter_file__quarter')
        .filter(is_current=True) 
        .order_by('sheet_name_slug', '-quarter_file__quarter__number')
        )
    
    # Filtrar para manter apenas o primeiro CSV por slug
    seen_slugs = set()
    chart_slugs = []

    # Populate this object
    sections = {}
    
    for csv in latest_csvs:
        slug = csv.sheet_name_slug
        if slug not in seen_slugs:
            seen_slugs.add(slug)

            chart_slugs.append({
                "slug": slug,
                "quarter_number": csv.quarter_file.quarter.number,
            })
            
            section_name = csv.quarter_file.section_name or "Sem Secção"

            if(sections.get(section_name) == None):
                sections[section_name] = []

            sections[section_name].append({
                "slug": slug,
                "quarter_number": csv.quarter_file.quarter.number,
            })

    return render(request, 'pages/home.html', {
        "app_context":{
            "qn":quarter.number,
            "quuid":quarter.uuid,            
        },
        'sections': sections,
        "empty":len(chart_slugs) <= 0,
        "chart_slugs": chart_slugs
    })

@login_required
def manage_quarters(request):
    quarters = Quarter.objects.filter(user=request.user)
    form = QuarterForm()

    if request.method == 'POST':
        form = QuarterForm(request.POST)
        if form.is_valid():
            quarter = form.save(commit=False)
            quarter.user = request.user 
            quarter.save()
            return redirect('manage_quarters')

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
def edit_quarter(request, uuid):
    quarter = get_object_or_404(Quarter, uuid=uuid, user=request.user)

    if request.method == 'POST':
        new_number = request.POST.get('number')
        if new_number:
            quarter.number = new_number
            quarter.user = request.user 
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
                # Podes fazer log, mostrar erro, ou armazenar numa lista para mostrar mais tarde
                print(f"Did not upload '{f.name}': {e}")
                continue

    return redirect('manage_quarters')

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