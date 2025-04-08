from django.contrib import admin

from .models import Quarter, ExcellFile, CSVFile


class CSVFileInline(admin.TabularInline):
    model = CSVFile
    extra = 0
    list_display = ('csv_path')


class ExcellFileInline(admin.TabularInline):
    model = ExcellFile
    extra = 1
    inlines = [CSVFileInline]  # Este truque não funciona diretamente

@admin.register(Quarter)
class QuarterAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'uuid', 'created_at')
    search_fields = ('number', 'uuid')
    ordering = ('-created_at',)
    inlines = [ExcellFileInline]

@admin.register(CSVFile)
class QuarterCSVAdmin(admin.ModelAdmin):
    list_display = ('sheet_name_slug','sheet_name','is_current','csv_path','quarter_file', 'quarter_uuid',)

@admin.register(ExcellFile)
class QuarterCSVAdmin(admin.ModelAdmin):
    list_display = ('quarter','is_processed','file','file_name','uploaded_at')
