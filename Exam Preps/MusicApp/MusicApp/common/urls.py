from django.urls import path, include

from MusicApp.common.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]