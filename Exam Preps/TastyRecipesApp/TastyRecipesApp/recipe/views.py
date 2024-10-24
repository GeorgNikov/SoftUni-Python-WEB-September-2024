from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from TastyRecipesApp.core.templatetags.get_user import get_user
from TastyRecipesApp.recipe.forms import RecipeCreateForm, RecipeEditForm
from TastyRecipesApp.recipe.models import Recipe


# Create your views here.
def recipe_details(request, pk):

    recipe = Recipe.objects.get(pk=pk)

    context = {
        'recipe': recipe,

    }

    return render(request, 'recipe/details-recipe.html', context)


def recipe_create(request, pk):
    profile = get_user()
    if request.method == 'POST':
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)  # Don't save yet
            recipe.author = profile  # Set the current user as the author
            recipe.save()  # Now save the recipe
            return redirect('catalogue')  # Redirect to some page after saving
    else:
        form = RecipeCreateForm(initial={'author': profile})  # Pre-populate hidden field with user ID


    context = {
        'form': form,
        'pk': pk,
        'profile': profile
    }

    return render(request, 'recipe/create-recipe.html', context)



def recipe_edit(request, pk):

    recipe = Recipe.objects.get(pk=pk)
    form = RecipeEditForm(request.POST or None, instance=recipe)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    form = RecipeEditForm(instance=recipe)

    context = {
        'form': form,
        'pk': pk,

    }

    return render(request, 'recipe/edit-recipe.html', context)


class DeleteRecipeView(DeleteView):
    model = Recipe

    template_name = 'recipe/delete-recipe.html'
    success_url = reverse_lazy('catalogue')
