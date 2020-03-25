from django.shortcuts import render
from django.shortcuts import render, redirect


def home(request):
	return render(request, 'testapp/home.html')
# Create your views here.
