from django.db import models

from TastyRecipesApp.core.choices import CuisineType
from TastyRecipesApp.core.validators import validate_cooking_time
from TastyRecipesApp.user_profile.models import Profile


# Create your models here.
# Recipe model
class Recipe(models.Model):

    title = models.CharField(
        max_length=100,
        unique=True,
        error_messages={'unique': 'We already have a recipe with the same title!'}
    )
    cuisine_type = models.CharField(
        max_length=7,
        choices=CuisineType.choices
    )
    ingredients = models.TextField(
        help_text="Ingredients must be separated by a comma and space."
    )
    instructions = models.TextField()
    cooking_time = models.PositiveIntegerField(
        validators=[validate_cooking_time],
        help_text="Provide the cooking time in minutes."
    )
    image_url = models.URLField(blank=True, null=True)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,  # If a profile is deleted, its associated recipes are deleted as well.
        related_name='recipes'
    )

    def __str__(self):
        return self.title