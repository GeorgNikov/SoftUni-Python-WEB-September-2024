from django.shortcuts import render, redirect

from FruitipediaApp.fruits.forms import CreateFruitForm, DeleteFruitForm, EditFruitForm
from FruitipediaApp.fruits.models import Fruit


# Create your views here.
def create_fruit(request):
    form = CreateFruitForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'fruit/create-fruit.html', context)


def details_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)

    context = {
        'fruit': fruit
    }

    return render(request, 'fruit/details-fruit.html', context)


def edit_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    form = EditFruitForm(instance=fruit)

    context = {
        'form': form
    }

    return render(request, 'fruit/edit-fruit.html', context)


def delete_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    form = DeleteFruitForm(request.POST or None, instance=fruit)

    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')


    context = {
        'form': form,
        'fruit': fruit
    }

    return render(request, 'fruit/delete-fruit.html', context)
