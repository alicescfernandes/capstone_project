from django import forms
from .models import Quarter

class QuarterForm(forms.ModelForm):
    class Meta:
        model = Quarter
        fields = ['number']
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-control upload-input', 'placeholder': 'Número do quarter'}),
        }
