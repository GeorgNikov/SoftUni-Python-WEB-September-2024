from django.urls import path
from djangointroduction.todo_app.views import index

urlpatterns = [
    path('', index),

]