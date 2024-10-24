# Class-based choices for cuisine types
from django.db import models


class CuisineType(models.TextChoices):
    FRENCH = 'French', 'French'
    CHINESE = 'Chinese', 'Chinese'
    ITALIAN = 'Italian', 'Italian'
    BALKAN = 'Balkan', 'Balkan'
    OTHER = 'Other', 'Other'