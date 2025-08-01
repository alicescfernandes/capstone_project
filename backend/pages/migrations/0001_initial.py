# Generated by Django 5.2 on 2025-04-19 22:40

import django.db.models.deletion
import pages.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('number', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quarters', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-number'],
                'unique_together': {('user', 'number')},
            },
        ),
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('file', models.FileField(upload_to=pages.models.user_quarter_upload_path)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('is_processed', models.BooleanField(default=False)),
                ('section_name', models.CharField(blank=True, editable=False, max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='excel_files', to=settings.AUTH_USER_MODEL)),
                ('quarter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='pages.quarter')),
            ],
            options={
                'unique_together': {('user', 'uuid')},
            },
        ),
        migrations.CreateModel(
            name='ChartData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('sheet_name_pretty', models.CharField(max_length=255)),
                ('sheet_name_slug', models.CharField(max_length=255)),
                ('quarter_uuid', models.UUIDField(editable=False, null=True)),
                ('is_current', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('data', models.JSONField(default=list)),
                ('column_order', models.JSONField(default=list)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='csv_data', to=settings.AUTH_USER_MODEL)),
                ('quarter_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='csvs', to='pages.excelfile')),
            ],
            options={
                'unique_together': {('user', 'uuid')},
            },
        ),
    ]
