from django.contrib import admin

from .models import Quarter, ExcelFile, CSVData
from unfold.admin import ModelAdmin


#@admin.register(MyModel)
#class CustomAdminClass(ModelAdmin):
#    pass

@admin.register(Quarter)
class QuarterAdmin(ModelAdmin):
    list_display = ('id', 'user', 'number', 'uuid', 'created_at')
    search_fields = ('number', 'uuid')
    ordering = ('-created_at',)
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user 
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
@admin.register(CSVData)
class CSVDataAdmin(ModelAdmin):
    list_display = ('sheet_name_slug','user','sheet_name_pretty','is_current','data','quarter_file', 'quarter_uuid','column_order')
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
@admin.register(ExcelFile)
class ExcelFileAdmin(ModelAdmin):
    list_display = ('quarter', 'user', 'is_processed', 'section_name', 'uploaded_at')
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)