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
        #ordering = ['-created_at']  # garante que o mais recente é o primeiro da lista
        ordering = ['-number']

    def __str__(self):
        return f"Q{self.number}"
    
    
class QuarterFile(models.Model):
    quarter = models.ForeignKey("Quarter", on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to=user_quarter_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} ({self.quarter})"