from django import forms

from MusicApp.mixins import PlaceholderMixin, ReadOnlyMixin
from MusicApp.albums.models import Album


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner',)


class CreateAlbumForm(PlaceholderMixin, AlbumBaseForm):
    pass


class EditAlbumForm(PlaceholderMixin, AlbumBaseForm):
    pass


class DetailsAlbumForm(ReadOnlyMixin, AlbumBaseForm):
    read_only_fields = ['album_name', 'artist', 'genre', 'price', 'description', 'image_url']


class DeleteAlbumForm(ReadOnlyMixin, AlbumBaseForm):
    read_only_fields = ['album_name', 'artist', 'genre', 'price', 'description', 'image_url']