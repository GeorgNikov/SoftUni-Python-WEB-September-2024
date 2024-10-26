from django import forms

from WoSApp.cars.models import Car
from WoSApp.profiles.models import Profile


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    year = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'type': 'text'}
        ),
    )

    price = forms.FloatField(
        widget=forms.TextInput(
            attrs={'type': 'text'}
        ),
    )


class CreateCarForm(BaseCarForm):
    image_url = forms.URLField(
        widget=forms.URLInput(
            attrs={'placeholder': 'https://...'}
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the owner to be the first Profile object and hide it from the form
        self.fields['owner'] = forms.ModelChoiceField(
            queryset=Profile.objects.all(),
            initial=Profile.objects.first(),
            widget=forms.HiddenInput()
        )

    def save(self, commit=True):
        # Set owner to Profile.objects.first() if it's not already set
        if not self.instance.owner:
            self.instance.owner = Profile.objects.first()
        return super().save(commit=commit)


class EditCarForm(BaseCarForm):
    pass


class DeleteCarForm(BaseCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the owner to be the first Profile object and hide it from the form
        self.fields['owner'] = forms.ModelChoiceField(
            queryset=Profile.objects.all(),
            initial=Profile.objects.first(),
            widget=forms.HiddenInput()
        )

        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
