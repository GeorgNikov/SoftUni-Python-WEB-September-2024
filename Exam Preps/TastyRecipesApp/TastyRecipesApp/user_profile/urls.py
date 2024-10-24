

from django.urls import path, include
from . import views

urlpatterns = [
    path('', include([
        path('delete/', views.delete_profile, name='delete_profile'),
        path('edit/', views.edit_profile, name='edit_profile'),
        path('details/', views.details_profile, name='profile_details'),
        path('create/', views.create_profile, name='create_profile'),
    ])),
    # path('create/', views.create_profile, name='create_profile'),
    # path('edit/', views.edit_profile, name='edit_profile'),
    # path('delete/', views.delete_profile, name='delete_profile'),
    # path('details/', views.details_profile, name='profile_details'),
]