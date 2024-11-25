from django.core.validators import MinLengthValidator
from django.db import models

from FruitipediaApp.profiles.validators import name_starts_with_letter_validator


# Create your models here.
class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 25
    FIRST_NAME_MIN_LENGTH = 2

    LAST_NAME_MAX_LENGTH = 35
    LAST_NAME_MIN_LENGTH = 1

    EMAIL_MAX_LENGTH = 40

    PASSWORD_MAX_LENGTH = 20
    PASSWORD_MIN_LENGTH = 8
    PASSWORD_HELP_TEXT = "*Password length requirements: 8 to 20 characters"

    AGE_DEFAULT_VALUE = 18

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            name_starts_with_letter_validator,
        ],
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            name_starts_with_letter_validator,
        ],
        verbose_name='Last Name',
    )

    email = models.EmailField(
        max_length=EMAIL_MAX_LENGTH,
        unique=True,
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LENGTH,
        validators=[
            MinLengthValidator(PASSWORD_MIN_LENGTH),
        ],
        help_text=PASSWORD_HELP_TEXT
    )

    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image URL'
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        default=AGE_DEFAULT_VALUE
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"