from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from WoSApp.cars.choices import CarTypeChoices
from WoSApp.cars.validators import car_year_validator


# Create your models here.
class Car(models.Model):
    car_type = models.CharField(
        max_length=10,
        choices=CarTypeChoices.choices,
    )

    model = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(1)
        ]
    )

    year = models.IntegerField(
        validators=[
            car_year_validator
        ]
    )

    image_url = models.URLField(
        unique=True,
        error_messages={
            "unique": "This image URL is already in use! Provide a new one."
        },
        blank=False,
        null=False,
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(1.0)
        ],
        blank=False,
        null=False,
    )

    owner = models.ForeignKey(
        'profiles.Profile',
        on_delete=models.CASCADE,
        related_name="cars",
        blank=False,
    )