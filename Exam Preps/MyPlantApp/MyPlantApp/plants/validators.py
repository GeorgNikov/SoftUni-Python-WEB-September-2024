from django.core.exceptions import ValidationError


def only_letters_validator(value):
    '''  Checks if plant name contains only letters.'''
    if not value.isalpha():
        raise ValidationError("Plant name should contain only letters!")