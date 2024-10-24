from django.urls import path, include

from MyPlantApp.plants.views import index, create_plant, catalogue
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('create/', views.create_plant, name='create plant'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('details/<int:pk>/', views.plant_details, name='plant details'),
    path('edit/<int:pk>/', views.edit_plant, name='edit plant'),
    path('delete/<int:pk>/', views.delete_plant, name='delete plant'),
]