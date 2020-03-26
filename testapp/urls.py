from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
path('', views.home, name='testapp-home'),
path('upload/', views.upload, name='testapp-upload'),


]
