from django.contrib import admin

from djangointroduction.todo_app.models import Tasks


# Register your models here.
@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    pass