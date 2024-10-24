from django.db import models

from MyPlantApp.plants.choices import PlantTypeChoices
from MyPlantApp.plants.validators import only_letters_validator


# Create your models here.
class Plant(models.Model):
    plant_type = models.CharField(
        max_length=14,
        choices=PlantTypeChoices.choices,
        blank=False,
        null=False,
        verbose_name="Type"
    )

    name = models.CharField(
        max_length=20,
        validators=[
            only_letters_validator
        ],
        blank=False,
        null=False,
        verbose_name="Name"
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name="Image URL"
    )

    description = models.TextField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        blank=False,
        null=False,
    )