from django.db import models
import os
import uuid
from django.contrib.auth.models import User
import os
import uuid
import pandas as pd
from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage

def user_quarter_upload_path(instance, filename):
    instance.file_name = filename
    return os.path.join("uploads", str(instance.uuid), filename)

class Quarter(models.Model):
    number = models.PositiveIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        ordering = ['-number']

    def __str__(self):
        return f"Q{self.number}"
    

class ExcellFile(models.Model):
    quarter = models.ForeignKey("Quarter", on_delete=models.CASCADE, related_name="files")
    # file = models.FileField(upload_to=user_quarter_upload_path, max_length=255)
    file = models.FileField(upload_to=user_quarter_upload_path, max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    file_name = models.TextField(editable=False)
    
    def __str__(self):
        return f"{self.file.name} ({self.quarter})"

    def process_and_store_csv(self):        
        folder = os.path.join(settings.MEDIA_ROOT, 'uploads', str(self.uuid))
        xlsx_path = self.file.path
        self.file_name = self.file.name

        try:
            excel = pd.read_excel(xlsx_path, sheet_name=None)

            for sheet_name, df in excel.items():
                if df.empty:
                    continue

                # Limpeza do DataFrame
                df = df.dropna(how='all')
                df.columns = df.iloc[0]
                df = df[1:]
                df = df.reset_index(drop=True)
                df = df[~df.apply(lambda row: row.astype(str).str.contains("End of worksheet", case=False)).any(axis=1)]

                # Converter nome da folha para slug
                sheet_slug = sheet_name.lower().replace(' ', '_')

                CSVFile.objects.filter(
                    quarter_file__quarter=self.quarter,
                    sheet_name_slug=sheet_slug,
                    is_current=True
                ).update(is_current=False)

                name = f"{sheet_slug}.csv"
                csv_path = os.path.join(folder, name)
                
                # Have django deal with duplicate files and file names
                available_path = default_storage.get_available_name(csv_path)
                print("available_path", available_path)

                CSVFile.objects.create(
                    quarter_file=self,
                    sheet_name=sheet_name,
                    sheet_name_slug=sheet_slug,
                    quarter_uuid=self.quarter.uuid,
                    csv_path=available_path,
                    is_current=True  # Isto é redundante mas explícito
                )

                df.to_csv(available_path, index=False)

        except Exception as e:
            print(f"Erro a processar {xlsx_path}: {e}")

    def extract_section_from_filename(self):
        """
        Extrai o nome da secção com base no nome original do ficheiro.
        Exemplo: 'CustomerNeeds-Q2.xlsx' → 'customerneeds'
        """
        filename = os.path.basename(self.file.name)
        name = filename.split('-')[0]
        return name.lower()
    """
    TODO: Clean this up. This is here for reference
    def save(self, *args, **kwargs):
        original_name = os.path.basename(self.file.name)
        name, ext = os.path.splitext(original_name)
        new_filename = f"{name}_{self.uuid}{ext}"

        new_path = os.path.join("uploads", str(self.quarter.uuid), new_filename)

        # Garante que ficheiro anterior com o mesmo nome não existe
        full_path = os.path.join(settings.MEDIA_ROOT, new_path)
        if os.path.exists(full_path):
            os.remove(full_path)

        # Substitui o nome no objeto FileField
        self.file.name = new_filename
        self.file_name = new_filename

        super().save(*args, **kwargs)
    """

class CSVFile(models.Model):
    quarter_file = models.ForeignKey("ExcellFile", on_delete=models.CASCADE, related_name="csvs")
    sheet_name = models.CharField(max_length=255)
    sheet_name_slug = models.CharField(max_length=255)
    csv_path = models.FilePathField(path=settings.MEDIA_ROOT, max_length=500)
    quarter_uuid = models.UUIDField(null=True, editable=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_current = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sheet_name} ({self.uuid})"
