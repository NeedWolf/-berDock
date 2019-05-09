from django.shortcuts import render
from django.views.generic import ListView,  DetailView, UpdateView
from django.views.generic.edit import CreateView
from home.models import App, AppRequest, AddComment, Comment
from . import models
from django.http import HttpResponseRedirect, HttpResponseBadRequest
# Create your views here.

class AppView(ListView):
    model = App
    paginate_by = 50
    template_name = 'home/index.html'

class AppDetailView(DetailView):
    model = App
    template_name = 'com_new.html'
    context_object_name = 'app_detail'

class AppCreateView(CreateView):
    model = App
    template_name = 'post_new.html'
    fields = '__all__'

class AppUpdateView(UpdateView):
    model = App
    fields = ['title', 'body', ]
    template_name = 'post_detail.html'

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

class AllappCreateView(CreateView):
    model = AppRequest
    template_name = 'apost_new.html'
    fields = '__all__'

class AllappView(ListView):
    model = AppRequest
    paginate_by = 50
    template_name = 'all_app.html'

class AllappDetailView(DetailView):
    model = AppRequest
    template_name = 'apost_detail.html'
    context_object_name = 'anything_you_want'

class ComCreateView(CreateView):
    model = Comment
    template_name = 'com_new.html'
    fields = '__all__'

class CategoryView(ListView):
    template_name = 'home/index.html'

    def get_queryset(self):
        return App.objects.filter(category__name=self.kwargs['category'])

def post_comments_controller(request, identifier):
    from .forms import CommentForm
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        comment_obj = comment_form.save(commit=False)
        app = App.objects.get(title=identifier)
        comment_obj.author = request.user
        comment_obj.app = app
        comment_obj.save()
        return HttpResponseRedirect('/post/%s/' % app.pk)
    else:
        return HttpResponseBadRequest()