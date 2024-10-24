from django import forms

from TastyRecipesApp.user_profile.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = 'nickname', 'first_name', 'last_name', 'chef'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = 'nickname', 'first_name', 'last_name', 'chef', 'bio'


class DetailsProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = 'nickname', 'first_name', 'last_name', 'chef', 'bio'


