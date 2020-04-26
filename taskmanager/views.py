from django.shortcuts import render
from models import Tasks

# Create your views here.
def tasks(request):
	tasks = Tasks.objects.all()

	return render(request, 'taskmanager/tasks.html', {'tasks', tasks})