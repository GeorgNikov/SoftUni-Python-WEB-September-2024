from django.core.exceptions import ValidationError


def car_year_validator(value):
    if value < 1999 or value > 2030:
        raise ValidationError('Year must be between 1999 and 2030!')