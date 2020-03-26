from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'testapp/home.html')

def upload(request):
	return render(request, 'testapp/upload.html')

