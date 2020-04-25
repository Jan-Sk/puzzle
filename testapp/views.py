from django.shortcuts import render, redirect
from testapp.models import Players, Logi
from django.contrib import messages

# Create your views here.
def home(request):
	return render(request, 'testapp/home.html')

def register(request):
	if request.method == 'POST':
			username = request.POST['username']
			password =  request.POST['password']
			print(username)
			print(password)
			post = Players.objects.filter(username=username)
			print(post)
			if post.exists() == True:
				messages.warning(request, 'uname is already in use')
				return render(request, 'testapp/register.html')
			else:
				Players(username = username, password = password).save()
				Logi(username = username, action = "acc created").save()
				messages.success(request, 'acc created')

				return redirect("testapp-login")
	return render(request, 'testapp/register.html')

def login(request):
	if request.method == 'POST':
			username = request.POST['username']
			password =  request.POST['password']
			print(username)
			print(password)
			post = Players.objects.filter(username=username)
			print(post)

			if post:
				if post.first().password == password:
					request.session['username'] = username
					print(username)
					Logi(username = username, action = "logged in").save()
					print('ustawiona sesja')
					messages.success(request, 'logged in')
					return redirect("testapp-home")
				else:
					Logi(username = username, action = "wrong pass").save()
					messages.warning(request, 'wrong pass')
					return render(request, 'testapp/login.html')
			else:
				messages.warning(request, 'wrong pass')
				print('nieustawiona sesja')
				return render(request, 'testapp/login.html')
	return render(request, 'testapp/login.html')

def logout(request):
	try:
		username = request.session['username']
		Logi(username = username, action = "logged out").save()

		del request.session['username']
		messages.success(request, 'logged out')
	except:
		pass
	return render(request, 'testapp/login.html')

def upload(request):
	return render(request, 'testapp/upload.html')

def testarea(request):
	if request.session.has_key('username'):
		username = request.session['username']
		Logi(username = username, action = "accessed restricted area").save()
		messages.success(request, 'welcome in restricted area!')
		return render(request, 'testapp/testarea.html')
	else:
		messages.warning(request, 'first log in -> nie masz konta spierdalaj')
		return redirect("testapp-home")
	return render(request, 'testapp/testarea.html')