from django.core.exceptions import ValidationError


def capital_letter_validator(value):
    ''' Checks if name starts with capital letter '''
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")