from django import forms

from MyPlantApp.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(ProfileBaseForm):
    class Meta:
        model = Profile
        exclude = ['profile_picture']


class EditProfileForm(ProfileBaseForm):
    pass


class DeleteProfileForm(ProfileBaseForm):
    pass