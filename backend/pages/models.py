import os
import uuid
import pandas as pd
from django.db import models, transaction
from .utils.data_processing import run_pipeline_for_sheet, extract_section_name, convert_df_to_json, parse_sheet
from .utils.data_processing import run_pipeline_for_sheet, extract_section_name
from .utils.chart_classification import ADDITIONAL_PROCESSING_PIPELINE
from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


User = get_user_model()

def user_quarter_upload_path(instance, filename):
    instance.section_name = extract_section_name(filename)
    return os.path.join("uploads", str(instance.uuid), filename)

class Quarter(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quarters")
    float_precision = models.PositiveIntegerField(
        default=9,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    
    class Meta:
        ordering = ['-number']
        unique_together = ('user', 'number')

    def __str__(self):
        return f"Q{self.number}"
    

class ExcelFile(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    quarter = models.ForeignKey("Quarter", on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to=user_quarter_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False, editable=True)
    section_name = models.CharField(max_length=255, editable=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="excel_files")
    
    class Meta:
        unique_together = ('user', 'uuid')
        
    def __str__(self):
        return f"{self.file.name} ({self.quarter})"

    def process_and_store_csv(self):
        # Do not "save" itself, instead update just this field. Calling .save() causes a recursion
        ExcelFile.objects.filter(pk=self.pk).update(is_processed=False)

        xlsx_path = self.file.path

        try:
            xls = pd.ExcelFile(xlsx_path)

            for sheet_name in xls.sheet_names:
                df_raw = parse_sheet(xls, sheet_name)
                if df_raw.empty:
                    continue

                processed_data_frame, sheet_slug, sheet_title  = run_pipeline_for_sheet(df_raw, sheet_name)

                # Get the column order first, this will be saved in a specific field
                if(sheet_slug in ADDITIONAL_PROCESSING_PIPELINE):
                    processing_functions= ADDITIONAL_PROCESSING_PIPELINE[sheet_slug]
                    df_processing = processed_data_frame
                    
                    for fn in processing_functions:
                        df_processing = fn(df_processing, self.quarter)
                    
                    processed_data_frame = df_processing

                columns = processed_data_frame.columns.tolist()
                data_json = convert_df_to_json(processed_data_frame, self.quarter.float_precision)
                
                # Check for other Chart Data's and mark them as not active
                ChartData.objects.filter(
                    quarter_file__quarter=self.quarter,
                    sheet_name_slug=sheet_slug,
                    is_current=True,
                    user=self.user
                ).update(is_current=False)

                ChartData.objects.create(
                    quarter_file=self,
                    sheet_name_pretty=sheet_title,
                    sheet_name_slug=sheet_slug,
                    quarter_uuid=self.quarter.uuid,
                    data=data_json,
                    is_current=True,
                    column_order=columns, 
                    user=self.user,
                )
        
            # Do not "save" itself, instead update just this field. Calling .save() causes a recursion
            ExcelFile.objects.filter(pk=self.pk).update(is_processed=True)

        except Exception as e:
            print(f"Erro a processar {xlsx_path}: {e}")

    # When deleting a file, if a bunch of "active" chart_data's originated from said file are the most up to date, 
    # then we need to update the active ones so that the user can still see something
    def delete(self, *args, **kwargs):
            related_chart_data = list(self.chart_data.filter(user=self.user))
            quarter = self.quarter
            excel_file_id = self.id

            # Build a set of slugs where the current chart_data is going to be deleted
            current_slugs = {
                chart_data.sheet_name_slug
                for chart_data in related_chart_data
                if chart_data.is_current
            }


            with transaction.atomic():
                super().delete(*args, **kwargs)

                for slug in current_slugs:
                    # Get the most recent ChartData (by upload date) for this slug in this quarter
                    recent_csv = (
                        ChartData.objects
                        .filter(
                            quarter_file__quarter=quarter,
                            sheet_name_slug=slug,
                            user=self.user,
                        )
                        .exclude(quarter_file__id=excel_file_id)
                        .order_by('-quarter_file__uploaded_at') 
                        .first()
                    )

                    if recent_csv:
                        recent_csv.is_current = True
                        recent_csv.save(update_fields=['is_current'])

class ChartData(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    quarter_file = models.ForeignKey("ExcelFile", on_delete=models.CASCADE, related_name="chart_data")
    
    # Sheet name (derived from she actual sheet title) is a more human-like string, that removes some text.
    sheet_name_pretty = models.CharField(max_length=255)
    # Sheet slug is a slug-like string derived from the sheet title, keeping in mind that the user won't change the sheet title, it groups the data into common identifiers
    sheet_name_slug = models.CharField(max_length=255)
    quarter_uuid = models.UUIDField(null=True, editable=False) # might be useful to remove the quarter_uuid and use the relations instead
    is_current = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField(default=list)
    column_order = models.JSONField(default=list) # saves the column order. this is crucial for the read from the API
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="csv_data")
    class Meta:
        unique_together = ('user', 'uuid')
        
    def __str__(self):
        return f"{self.sheet_name_pretty} ({self.uuid})"
