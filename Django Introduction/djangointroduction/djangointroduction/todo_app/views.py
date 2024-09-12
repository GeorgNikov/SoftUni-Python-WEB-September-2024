from django.shortcuts import render

from djangointroduction.todo_app.models import Tasks


# Create your views here.
def index(request):
    title_filter = request.GET.get('title_filter', '')

    if title_filter:
        tasks = Tasks.objects.filter(name__icontains=title_filter)
    else:
        tasks = Tasks.objects.all()

    context = {
        'title_filter': title_filter,
        'tasks': tasks
    }

    return render(request, 'tasks/index.html', context)