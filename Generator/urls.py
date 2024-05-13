from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'Generator'

urlpatterns = [
    path("", include('django.contrib.auth.urls')),
    path("", views.index, name='index'),

]