from django import forms
from MyPlantApp.plants.models import Plant


class BasePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class CreatePlantForm(BasePlantForm):
    pass


class EditPlantForm(BasePlantForm):
    price = forms.FloatField(
        widget=forms.TextInput(
            attrs={'type': 'text'}
        ),
    )


class DeletePlantForm(BasePlantForm):
    price = forms.FloatField(
        widget=forms.TextInput(
            attrs={'type': 'text'}
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'


