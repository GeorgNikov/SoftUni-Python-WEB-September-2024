# Custom validators
from django.core.exceptions import ValidationError


def validate_nickname_length(value):
    if len(value) < 2:
        raise ValidationError("Nickname must be at least 2 chars long!")

def validate_name_capitalized(value):
    if not value[0].isupper():
        raise ValidationError("Name must start with a capital letter!")

def validate_cooking_time(value):
    if value < 1:
        raise ValidationError("Time cannot be below 1.")