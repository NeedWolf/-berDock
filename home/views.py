from django.shortcuts import render
from django.views.generic import ListView
from .models import App
from django.http import HttpResponse
# Create your views here.

class AppView(ListView):
    model = App
    template_name = 'home/index.html'