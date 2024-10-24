from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', include([
        path('create/', views.recipe_create, name='create_recipe'),
        path('details/', views.recipe_details, name='recipe_details'),
        path('edit/', views.recipe_edit, name='edit_recipe'),
        path('delete/', views.DeleteRecipeView.as_view(), name='delete_recipe'),
    ])),
]