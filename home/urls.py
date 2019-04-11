from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.AppView.as_view(), name='index')
]