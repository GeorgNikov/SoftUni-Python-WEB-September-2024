from django import forms

from WoSApp.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(ProfileBaseForm):
    age = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'type': 'text'}
        ),
        help_text="Age requirement: 21 years and above.",
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'type': 'password'}
        ),

    )

    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']



class EditProfileForm(ProfileBaseForm):
    age = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'type': 'text'}
        ),
    )


class DeleteProfileForm(ProfileBaseForm):
    pass