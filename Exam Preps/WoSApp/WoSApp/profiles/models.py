from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from WoSApp.profiles.validators import only_letters_digits_underscore_validator


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(3, "Username must be at least 3 chars long!"),
            only_letters_digits_underscore_validator,
        ],

    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(21, "Age requirement: 21 years and above.")
        ]
    )

    password = models.CharField(
        max_length=20,
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        verbose_name="First Name",
    )

    last_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
        verbose_name="Last Name",
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
        verbose_name="Profile Picture",
    )

    @property
    def full_name(self):
        if self.first_name and not self.last_name:
            return self.first_name
        elif not self.first_name and self.last_name:
            return self.last_name
        elif not self.first_name and not self.last_name:
            return ""
        return f"{self.first_name} {self.last_name}"
