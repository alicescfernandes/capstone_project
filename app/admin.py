from django.contrib import admin
from .models import Chart

@admin.register(Chart)
class ChartAdmin(admin.ModelAdmin):
    list_display = ('title', 'chart_type', 'is_active', 'created_at')
    list_filter = ('chart_type', 'is_active')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    
    def save_model(self, request, obj, form, change):
        if not obj.config:
            obj.config = obj.get_default_config()
        super().save_model(request, obj, form, change)
