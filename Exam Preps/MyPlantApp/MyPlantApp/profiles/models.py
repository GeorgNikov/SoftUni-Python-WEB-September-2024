from django.core.validators import MinLengthValidator
from django.db import models

from MyPlantApp.profiles.validators import capital_letter_validator


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(2)
        ],
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=20,
        validators=[
            capital_letter_validator
        ],
        blank=False,
        null=False,
        verbose_name="First Name"
    )

    last_name = models.CharField(
        max_length=20,
        validators=[
            capital_letter_validator
        ],
        blank=False,
        null=False,
        verbose_name="Last Name"
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
        verbose_name="Profile Picture"
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"