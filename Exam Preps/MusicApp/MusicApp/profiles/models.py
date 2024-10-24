from django.core.validators import MinLengthValidator
from django.db import models

from MusicApp.profiles.validators import AlphaNumericValidator


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            AlphaNumericValidator(),
        ]
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
