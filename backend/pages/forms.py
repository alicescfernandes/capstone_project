from django import forms
from .models import ExcellFile

class MultiFileUploadForm(forms.ModelForm):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = ExcellFile
        fields = ['files']

    def save(self, quarter, commit=True):
        # Guarda múltiplos ficheiros associados ao mesmo quarter
        files = self.files.getlist('files')
        instances = []
        for file in files:
            instance = ExcellFile(quarter=quarter, file=file)
            if commit:
                instance.save()
            instances.append(instance)
        return instances