from django.core.validators import MinLengthValidator
from django.db import models

from FruitipediaApp.fruits.validators import only_letters_validator


# Create your models here.
class Fruit(models.Model):
    NAME_MAX_LENGTH = 30
    NAME_MIN_LENGTH = 2
    NAME_UNIQUE_ERROR_MESSAGE = "This fruit name is already in use! Try a new one."

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        validators=[
            MinLengthValidator(NAME_MIN_LENGTH),
            only_letters_validator,
        ],
        error_messages={
            'unique': NAME_UNIQUE_ERROR_MESSAGE,
        },
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )

    description = models.TextField(
    )

    nutrition = models.TextField(
        null=True,
        blank=True,

    )

    owner = models.ForeignKey(
        'profiles.Profile',
        on_delete=models.CASCADE,
        related_name='fruits',
    )