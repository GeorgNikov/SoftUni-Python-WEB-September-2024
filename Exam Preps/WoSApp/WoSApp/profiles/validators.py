from django.core.exceptions import ValidationError


def only_letters_digits_underscore_validator(value):
    if not value.isalnum() or "_" in value:
        raise ValidationError("Username must contain only letters, digits, and underscores!")