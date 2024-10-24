import re

from django.utils.deconstruct import deconstructible
from django.utils.text import slugify


def alpha_numeric_validator(value):
    if not re.match(r'^[\w_]+$', value):
        raise ValueError("Ensure this value contains only letters, numbers, and underscore.")


@deconstructible
class AlphaNumericValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Ensure this value contains only letters, numbers, and underscore."
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        if "-" in value or value.lower() != slugify(value):
            raise ValueError(self.message)