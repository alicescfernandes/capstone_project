import os
import shutil
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from .models import Quarter, ExcelFile, CSVData

@receiver(post_save, sender=ExcelFile)
def process_file_on_upload(sender, instance, created, **kwargs):
    instance.process_and_store_csv()