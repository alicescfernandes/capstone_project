# serializers.py
from rest_framework import serializers
from .models import Quarter

class QuarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quarter
        fields = ['number', 'uuid', 'created_at']
