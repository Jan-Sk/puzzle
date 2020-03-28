from django.shortcuts import render, redirect
from testapp.models import Players

# Create your views here.
def home(request):
	return render(request, 'testapp/home.html')

def register(request):
	return render(request, 'testapp/register.html')

def login(request):
	if request.method == 'POST':
	        username = request.POST['username']
	        password =  request.POST['password']
	        post = Players.objects.filter(player=username)


	        if post:
	        	request.session['username'] = username
	        	print('ustawiona sesja')
	        	return redirect("testapp-home")
	        else:
	        	print('nieustawiona sesja')
	        	return render(request, 'testapp/login.html')

	return render(request, 'testapp/login.html')

def upload(request):
	return render(request, 'testapp/upload.html')

def debil(request):
	return render(request, 'testapp/debil.html')