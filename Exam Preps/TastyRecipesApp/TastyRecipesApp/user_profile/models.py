from django.db import models
from TastyRecipesApp.core.validators import validate_nickname_length, validate_name_capitalized


# Profile model
class Profile(models.Model):
    nickname = models.CharField(
        max_length=20,
        unique=True,
        validators=[validate_nickname_length],
        error_messages={'unique': 'This nickname is already taken.'}
    )
    first_name = models.CharField(
        max_length=30,
        validators=[validate_name_capitalized]
    )
    last_name = models.CharField(
        max_length=30,
        validators=[validate_name_capitalized]
    )
    chef = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nickname