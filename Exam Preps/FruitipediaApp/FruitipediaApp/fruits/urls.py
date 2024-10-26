

from django.urls import path, include

from FruitipediaApp.fruits.views import create_fruit, details_fruit, delete_fruit, edit_fruit

urlpatterns = [
    path('create/', create_fruit, name='create fruit'),
    path('<int:pk>/', include([
        path('details/', details_fruit, name='fruit details'),
        path('delete/', delete_fruit, name='delete fruit'),
        path('edit/', edit_fruit, name='edit fruit'),
    ]))
]
