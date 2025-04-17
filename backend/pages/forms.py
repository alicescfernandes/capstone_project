from django import forms
from .models import ExcelFile

""" class MultiFileUploadForm(forms.ModelForm):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = ExcelFile
        fields = ['files']

    def save(self, quarter, commit=True):
        # Guarda múltiplos ficheiros associados ao mesmo quarter
        files = self.files.getlist('files')
        instances = []
        for file in files:
            instance = ExcelFile(quarter=quarter, file=file)
            if commit:
                instance.save()
            instances.append(instance)
        return instances """
    
from django import forms
from .models import Quarter

class QuarterForm(forms.ModelForm):
    class Meta:
        model = Quarter
        fields = ['number']
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número do quarter'}),
        }
