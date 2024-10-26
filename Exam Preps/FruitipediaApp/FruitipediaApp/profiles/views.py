from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect

from FruitipediaApp.fruits.models import Fruit
from FruitipediaApp.profiles.forms import CreateProfileForm, EditProfileForm
from FruitipediaApp.profiles.models import Profile


# Create your views here.
def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'profile/create-profile.html', context)


def details_profile(request):
    profile = Profile.objects.first()

    if not profile:
        return redirect('create profile')

    context = {
        'profile': profile
    }
    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    form = EditProfileForm(request.POST or None, instance=profile)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form
    }

    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    if request.method == 'POST':
        Profile.objects.all().delete()
        Fruit.objects.all().delete()
        return redirect('index')
    return render(request, 'profile/delete-profile.html')