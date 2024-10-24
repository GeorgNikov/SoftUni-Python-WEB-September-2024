from django.db import models


class MusicGenre(models.TextChoices):
    POP = 'Pop', 'Pop Music'
    JAZZ = 'Jazz', 'Jazz Music'
    RNB = 'R&B', 'R&B Music'
    ROCK = 'Rock', 'Rock Music'
    COUNTRY = 'Country', 'Country Music'
    DANCE = 'Dance', 'Dance Music'
    HIPHOP = 'HipHop', 'Hip Hop Music'
    OTHER = 'Other', 'Other'