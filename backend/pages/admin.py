from django.contrib import admin

from .models import Quarter, ExcelFile, CSVData


class CSVDataInline(admin.TabularInline):
    model = CSVData
    extra = 0
    list_display = ('csv_path')


class ExcelFileInline(admin.TabularInline):
    model = ExcelFile
    extra = 1
    inlines = [CSVDataInline]  # Este truque não funciona diretamente

@admin.register(Quarter)
class QuarterAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'uuid', 'created_at')
    search_fields = ('number', 'uuid')
    ordering = ('-created_at',)
    inlines = [ExcelFileInline]

@admin.register(CSVData)
class QuarterCSVAdmin(admin.ModelAdmin):
    list_display = ('sheet_name_slug','sheet_name','is_current','csv_path','quarter_file', 'quarter_uuid',)

@admin.register(ExcelFile)
class ExcelFileAdmin(admin.ModelAdmin):
    list_display = ('quarter','is_processed','section_name','uploaded_at')
