from django.shortcuts import render, redirect

from MyPlantApp.plants.forms import CreatePlantForm, EditPlantForm, DeletePlantForm
from MyPlantApp.plants.models import Plant


# Create your views here.
def index(request):
    return render(request, 'common/home-page.html')


def catalogue(request):
    plants = Plant.objects.all()

    context = {
        'plants': plants
    }

    return render(request, 'common/catalogue.html', context)


def create_plant(request):
    plants = Plant.objects.all()
    form = CreatePlantForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'plants': plants,
        'form': form
    }
    return render(request, 'plants/create-plant.html', context)


def plant_details(request, pk):
    plant = Plant.objects.get(pk=pk)

    context = {
        'plant': plant
    }
    return render(request, 'plants/plant-details.html', context)


def edit_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    form = EditPlantForm(request.POST or None, instance=plant)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'plant': plant,
        'form': form
    }

    return render(request, 'plants/edit-plant.html', context)


def delete_plant(request, pk):
    plant = Plant.objects.get(pk=pk)

    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')
    else:
        form = DeletePlantForm(instance=plant)

    context = {
        'form': form,
        'plant': plant
    }

    return render(request, 'plants/delete-plant.html', context)