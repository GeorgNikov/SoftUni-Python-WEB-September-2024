from django import forms

from MusicApp.mixins import PlaceholderMixin
from MusicApp.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(PlaceholderMixin, ProfileBaseForm):
    pass


class EditProfileForm(PlaceholderMixin, ProfileBaseForm):
    pass


class DeleteProfileForm(PlaceholderMixin, ProfileBaseForm):
    pass