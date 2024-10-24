from django.shortcuts import render, redirect

from TastyRecipesApp.core.templatetags.get_user import get_user
from TastyRecipesApp.recipe.models import Recipe
from TastyRecipesApp.user_profile.forms import CreateProfileForm, EditProfileForm


# Create your views here.

def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'profile/create-profile.html', context)


def edit_profile(request):
    profile = get_user()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = get_user()

    if request.method == 'POST':
        profile.delete()
        Recipe.objects.all().delete()
        return redirect('catalogue')

    context = {
        'profile': profile
    }

    return render(request, 'profile/delete-profile.html', context)


def details_profile(request):
    profile = get_user()

    context = {
        'profile': profile
    }
    return render(request, 'profile/details-profile.html', context)
