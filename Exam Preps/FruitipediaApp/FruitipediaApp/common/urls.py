from django.urls import path, include

from FruitipediaApp.common.views import index, dashboard

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),

]
