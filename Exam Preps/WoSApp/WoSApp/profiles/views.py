from django.shortcuts import render, redirect

from WoSApp.cars.models import Car
from WoSApp.common.templatetags.get_user import get_user
from WoSApp.profiles.forms import CreateProfileForm, EditProfileForm
from WoSApp.profiles.models import Profile


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

    return render(request, 'profile/profile-create.html', context)


def profile_details(request):
    cars = Car.objects.all()
    total_sum = sum([car.price for car in cars])

    context = {
        'cars': cars,
        'total_sum': total_sum
    }

    return render(request, 'profile/profile-details.html', context)


def profile_edit(request):
    form = EditProfileForm(request.POST or None, instance=get_user())

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form
    }

    return render(request, 'profile/profile-edit.html', context)


def profile_delete(request):
    if request.method == 'POST':
        Profile.objects.all().delete()
        Car.objects.all().delete()
        return redirect('index')
    return render(request, 'profile/profile-delete.html')
