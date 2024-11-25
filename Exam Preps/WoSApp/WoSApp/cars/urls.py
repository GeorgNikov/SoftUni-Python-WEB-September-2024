

from django.urls import path, include
from . import views


urlpatterns = [


    path('catalogue/', views.catalogue, name='catalogue'),
    path('create/', views.car_create, name='car create'),
    path('<int:id>/', include([
        path('details/', views.car_details, name='car details'),
        path('edit/', views.car_edit, name='car edit'),
        path('delete/', views.car_delete, name='car delete'),
    ])),


]