from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_profile, name='create profile'),
    path('edit/', views.edit_profile, name='edit profile'),
    path('details/', views.profile_details, name='profile details'),
    path('delete/', views.delete_profile, name='delete profile'),
]