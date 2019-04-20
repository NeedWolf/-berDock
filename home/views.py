from django.shortcuts import render
from django.views.generic import ListView,  DetailView

from django.views.generic.edit import CreateView
from .models import App
from django.http import HttpResponse
# Create your views here.

class AppView(ListView):
    model = App
    paginate_by = 50
    template_name = 'home/index.html'

# class AppCreateView(CreateView):
#     model = App
#     template_name = 'post_new.html'
#     fields = '__all__'
#
# class AppDetailView(DetailView):
#     model = App
#     template_name = 'all_app.html'
#     context_object_name = 'anything_you_want'


class SearchView(ListView):
    model = App
    paginate_by = 50
    template_name = 'home/search.html'

    def get_queryset(self):
        filter_val = self.request.GET.get('search', '')
        new_context = App.objects.filter(title__contains=filter_val)
        return new_context

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

class AllappView(ListView):
    model = App
    paginate_by = 50
    template_name = 'all_app.html'

class AllappDetailView(DetailView):
    model = App
    template_name = 'post_detail.html'
    context_object_name = 'anything_you_want'

class AllappCreateView(CreateView):
    model = App
    template_name = 'post_new.html'
    fields = '__all__'

