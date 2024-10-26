from django.shortcuts import render, redirect

from WoSApp.cars.forms import CreateCarForm, DeleteCarForm
from WoSApp.cars.models import Car


# Create your views here.

def catalogue(request):
    cars = Car.objects.all()

    context = {
        'cars': cars
    }

    return render(request, 'car/catalogue.html', context)


def car_create(request):
    cars = Car.objects.all()
    form = CreateCarForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'cars': cars
    }

    return render(request, 'car/car-create.html', context)


def car_details(request, id):
    car = Car.objects.get(id=id)

    context = {
        'car': car
    }

    return render(request, 'car/car-details.html', context)


def car_edit(request, id):
    car = Car.objects.get(id=id)

    if request.method == 'POST':
        form = CreateCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    form = CreateCarForm(instance=car)

    context = {
        'form': form
    }

    return render(request, 'car/car-edit.html', context)


def car_delete(request, id):
    car = Car.objects.get(id=id)

    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')

    form = DeleteCarForm(instance=car)

    context = {
        'form': form
    }
    return render(request, 'car/car-delete.html', context)