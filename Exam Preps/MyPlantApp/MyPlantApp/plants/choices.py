from django.db import models


class PlantTypeChoices(models.TextChoices):
    OUTDOOR = "Outdoor Plants", "Outdoor Plants"
    INDOOR = "Indoor Plants", "Indoor Plants"