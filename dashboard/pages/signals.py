import os
import shutil
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from .models import Quarter

@receiver(post_save, sender=Quarter)
def create_quarter_directory(sender, instance, created, **kwargs):
    if created:
        path = os.path.join(settings.MEDIA_ROOT, 'uploads', str(instance.uuid))
        os.makedirs(path, exist_ok=True)

@receiver(post_delete, sender=Quarter)
def delete_quarter_directory(sender, instance, **kwargs):
    path = os.path.join(settings.MEDIA_ROOT, 'uploads', str(instance.uuid))
    if os.path.isdir(path):
        shutil.rmtree(path)
        
