import os
import shutil
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from .models import Quarter, ExcellFile, CSVFile

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
        
        
@receiver(post_delete, sender=ExcellFile)
def delete_files_on_ExcellFile_delete(sender, instance, **kwargs):
    if instance.file and os.path.exists(instance.file.path):
        os.remove(instance.file.path)
            
@receiver(post_delete, sender=CSVFile)
def delete_csv_file_from_disk(sender, instance, **kwargs):
    if instance.csv_path and os.path.exists(instance.csv_path):
        os.remove(instance.csv_path)

@receiver(post_save, sender=ExcellFile)
def process_file_on_upload(sender, instance, created, **kwargs):
    if created:
        instance.process_and_store_csv()
