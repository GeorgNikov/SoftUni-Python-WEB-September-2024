from django import forms


from TastyRecipesApp.recipe.models import Recipe


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('author',)


class RecipeEditForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('author',)