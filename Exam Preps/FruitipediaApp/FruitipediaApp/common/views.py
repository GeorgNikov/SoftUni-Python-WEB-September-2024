from django.shortcuts import render, redirect

from FruitipediaApp.fruits.models import Fruit
from FruitipediaApp.profiles.models import Profile


# Create your views here.
def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    profile = Profile.objects.first()
    fruits = Fruit.objects.all()

    if not profile:
        return redirect('create profile')

    context = {
        'fruits': fruits
    }

    return render(request, 'common/dashboard.html', context)