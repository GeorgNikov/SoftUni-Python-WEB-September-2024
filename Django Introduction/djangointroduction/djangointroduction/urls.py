"""
STEP 1: Create a project
STEP 2: Create a app
STEP 3:
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
