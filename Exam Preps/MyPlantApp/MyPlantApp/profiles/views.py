from django.shortcuts import render, redirect

from MyPlantApp.common.templatetags.get_user import get_user
from MyPlantApp.plants.models import Plant
from MyPlantApp.profiles.forms import CreateProfileForm, EditProfileForm


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

    return render(request, 'profiles/create-profile.html', context)


def profile_details(request):
    plants = Plant.objects.all()

    context = {
        'plants': plants
    }

    return render(request, 'profiles/profile-details.html', context)


def edit_profile(request):
    form = EditProfileForm(request.POST or None, instance=get_user())

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form
    }

    return render(request, 'profiles/edit-profile.html', context)


def delete_profile(request):
    if request.method == 'POST':
        get_user().delete()
        Plant.objects.all().delete()
        return redirect('index')
    return render(request, 'profiles/delete-profile.html')