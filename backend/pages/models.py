from django.db import models
import os
import uuid
from django.contrib.auth.models import User

# Create your models here.
def user_quarter_upload_path(instance, filename):
    # Caminho: media/uploads/<uuid4>/<filename>
    return os.path.join("uploads", str(instance.quarter.uuid), filename)

class Quarter(models.Model):
    number = models.PositiveIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        ordering = ['-number']

    def __str__(self):
        return f"Q{self.number}"
    
    
import os
import uuid
import pandas as pd
from django.db import models
from django.conf import settings

def user_quarter_upload_path(instance, filename):
    return os.path.join("uploads", str(instance.quarter.uuid), filename)

class QuarterFile(models.Model):
    quarter = models.ForeignKey("Quarter", on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to=user_quarter_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} ({self.quarter})"

    def process_and_store_csv(self):
        """
        Converte todas as sheets do ficheiro XLSX para CSVs normalizados.
        Guarda-os em: /uploads/<uuid>/<nome_conhecido>_q<numero>.csv
        """
        section_name = self.extract_section_from_filename()
        quarter_number = self.quarter.number
        folder = os.path.join(settings.MEDIA_ROOT, 'uploads', str(self.quarter.uuid))

        xlsx_path = self.file.path
        try:
            excel = pd.read_excel(xlsx_path, sheet_name=None)
            for sheet_name, df in excel.items():
                if df.empty:
                    continue
                df = df.dropna(how='all')  # remove linhas vazias
                df.columns = df.iloc[0]    # primeira linha como header
                df = df[1:]                # remove a linha do header
                df = df.reset_index(drop=True)

                name = f"{section_name}_{sheet_name.lower().replace(' ', '_')}_q{quarter_number}.csv"
                csv_path = os.path.join(folder, name)

                df.to_csv(csv_path, index=False)

                #  Eliminar o ficheiro XLSX original
                if os.path.exists(xlsx_path):
                    os.remove(xlsx_path)

        except Exception as e:
            # TODO: logar ou lançar exceção visível
            print(f"Erro a processar {xlsx_path}: {e}")

    def extract_section_from_filename(self):
        """
        Extrai o nome da secção com base no nome original do ficheiro.
        Exemplo: 'CustomerNeeds-Q2.xlsx' → 'customerneeds'
        """
        filename = os.path.basename(self.file.name)
        name = filename.split('-')[0]
        return name.lower()
