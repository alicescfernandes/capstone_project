import json

from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Quarter, ExcelFile, ChartData
from django.db import models
from django.utils.html import format_html

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

@admin.register(ChartData)
class ChartDataAdmin(ModelAdmin):
    list_display = (
        'sheet_name_slug', 'user', 'sheet_name_pretty',
        'is_current', 'short_data', 'quarter_file', 'quarter_uuid', 'short_column_order'
    )
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

    def short_data(self, obj):
        try:
            pretty = json.dumps(obj.data, indent=2)
            return format_html('<pre style="max-height: 100px; overflow: auto;">{}…</pre>', pretty[:500])
        except Exception:
            return "[invalid JSON]"
        
    def short_column_order(self, obj):
        try:
            pretty = json.dumps(obj.column_order, indent=2)
            return format_html('<pre style="max-height: 100px; overflow: auto;">{}…</pre>', pretty[:500])
        except Exception:
            return "[invalid JSON]"



    short_data.short_description = 'data'
    short_column_order.short_description = 'column_order'
    
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