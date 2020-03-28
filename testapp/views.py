from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'testapp/home.html')

def register(request):
	return render(request, 'testapp/register.html')

def login(request):
	return render(request, 'testapp/login.html')

def upload(request):
	return render(request, 'testapp/upload.html')

def tasks(request):
	return render(request, 'testapp/tasks.html')