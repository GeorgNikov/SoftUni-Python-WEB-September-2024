"""
STEP 1: Create a project
STEP 2: Create a app
STEP 3:
"""


from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangointroduction.todo_app.urls')),
]
