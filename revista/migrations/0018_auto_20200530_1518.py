# Generated by Django 3.0.6 on 2020-05-30 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0017_author_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(verbose_name='slug'),
        ),
    ]
