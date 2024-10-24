from django.shortcuts import render

from TastyRecipesApp.recipe.models import Recipe


# Create your views here.
# def get_profile():
#     profile = Profile.objects.first()
#     if profile:
#         recipes = Recipe.objects.all()
#     return profile


def index(request):
    return render(request, 'core/home-page.html')


def catalogue(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }
    return render(request, 'core/catalogue.html', context)
