# Generated by Django 3.1.1 on 2020-11-10 03:45

import advertisement.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image_mobile',
            field=models.ImageField(blank=True, upload_to=advertisement.models.Advertisement.m_path, verbose_name='Image - Mobile'),
        ),
    ]
