from rest_framework import serializers
from .models import Quarter

class QuarterSerializer(serializers.ModelSerializer):
    float_precision = serializers.IntegerField(min_value=1, max_value=10)
    class Meta:        
        model = Quarter
        fields = ['number', 'uuid', 'created_at', 'float_precision']
