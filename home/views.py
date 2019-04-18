from django.shortcuts import render
from django.views.generic import ListView
from .models import App
from django.http import HttpResponse
# Create your views here.

class AppView(ListView):
    model = App
    paginate_by = 50
    template_name = 'home/index.html'

    def get_queryset(self):
        filter_val = self.request.GET.get('search', '')
        new_context = App.objects.filter(title__contains=filter_val)
        return new_context

    def get_context_data(self, **kwargs):
        context = super(AppView, self).get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context