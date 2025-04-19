from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ExcelFile

@receiver(post_save, sender=ExcelFile)
def process_file_on_upload(sender, instance, created, **kwargs):
    instance.process_and_store_csv()
