from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
path('', views.home, name='testapp-home'),
path('upload/', views.upload, name='testapp-upload'),
path('register/', views.register, name='testapp-register'),
path('login/', views.login, name='testapp-login'),
path('logout/', views.logout, name='testapp-logout'),
path('testarea/', views.testarea, name='testapp-testarea'),
]
