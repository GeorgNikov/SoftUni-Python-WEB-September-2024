from django import forms

from FruitipediaApp.fruits.models import Fruit
from FruitipediaApp.profiles.models import Profile


class BaseFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
        label=''
    )

    image_url = forms.URLField(
        widget=forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
        label=''
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
        label=''
    )

    nutrition = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
        label=''
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the owner to be the first Profile object and hide it from the form
        self.fields['owner'] = forms.ModelChoiceField(
            queryset=Profile.objects.all(),
            initial=Profile.objects.first(),
            widget=forms.HiddenInput()
        )

class CreateFruitForm(BaseFruitForm):
    pass


class EditFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the owner to be the first Profile object and hide it from the form
        self.fields['owner'] = forms.ModelChoiceField(
            queryset=Profile.objects.all(),
            initial=Profile.objects.first(),
            widget=forms.HiddenInput()
        )


class DeleteFruitForm(BaseFruitForm):
    class Meta:
        model = Fruit
        exclude = ['nutrition']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nutrition'].widget = forms.HiddenInput()

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
