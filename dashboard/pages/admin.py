from django.contrib import admin

from .models import Quarter, QuarterFile

class QuarterFileInline(admin.TabularInline):
    model = QuarterFile
    extra = 1

@admin.register(Quarter)
class QuarterAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'uuid', 'created_at')
    search_fields = ('number', 'uuid')
    ordering = ('-created_at',)
    inlines = [QuarterFileInline]