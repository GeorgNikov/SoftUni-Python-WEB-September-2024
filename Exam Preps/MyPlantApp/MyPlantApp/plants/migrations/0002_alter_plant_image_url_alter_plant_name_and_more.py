# Generated by Django 5.1.2 on 2024-10-24 08:16

import MyPlantApp.plants.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='image_url',
            field=models.URLField(verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='name',
            field=models.CharField(max_length=20, validators=[MyPlantApp.plants.validators.only_letters_validator], verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='plant_type',
            field=models.CharField(choices=[('Outdoor Plants', 'Outdoor Plants'), ('Indoor Plants', 'Indoor Plants')], max_length=14, verbose_name='Type'),
        ),
    ]