from django import forms


from FruitipediaApp.profiles.models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'



class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'password')

    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
        label=''
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
        label=''
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
        label=''
    )
    password = forms.CharField(
        max_length=20,
        min_length=8,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        help_text='*Password length requirements: 8 to 20 characters',
        label=''
    )

class EditProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url', 'age')


class DeleteProfileForm(BaseProfileForm):
    pass
