from django.db import models
import json

class Chart(models.Model):
    CHART_TYPES = [
        ('line', 'Line Chart'),
        ('bar', 'Bar Chart'),
        ('pie', 'Pie Chart'),
        ('area', 'Area Chart'),
        ('scatter', 'Scatter Plot'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    chart_type = models.CharField(max_length=20, choices=CHART_TYPES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # JSON field to store chart configuration
    config = models.JSONField(default=dict, help_text="Chart configuration including data, labels, and styling")
    
    # Fields for data source configuration
    x_axis_label = models.CharField(max_length=100, blank=True)
    y_axis_label = models.CharField(max_length=100, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['chart_type']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return f"{self.title} ({self.get_chart_type_display()})"

    def get_chart_config(self):
        """Returns the chart configuration as a dictionary"""
        return self.config if isinstance(self.config, dict) else json.loads(self.config)

    def set_chart_config(self, config_dict):
        """Sets the chart configuration from a dictionary"""
        self.config = config_dict
        self.save()

    def get_default_config(self):
        """Returns a default configuration based on chart type"""
        base_config = {
            'height': 350,
            'toolbar': {'show': False},
        }
        
        if self.chart_type in ['line', 'bar', 'area']:
            return {
                **base_config,
                'type': self.chart_type,
                'series': [{'name': 'Data', 'data': []}],
                'xaxis': {'categories': []},
            }
        elif self.chart_type == 'pie':
            return {
                **base_config,
                'type': 'pie',
                'series': [],
                'labels': [],
            }
        elif self.chart_type == 'scatter':
            return {
                **base_config,
                'type': 'scatter',
                'series': [{'name': 'Data', 'data': []}],
                'xaxis': {'type': 'numeric'},
                'yaxis': {'type': 'numeric'},
            }
        return base_config
