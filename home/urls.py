
from django.urls import path
from . import views

urlpatterns = [

  path('', views.AppView.as_view(), name='index'),
  path('results/', views.SearchView.as_view(), name='search'),
  path('allapps/', views.AllappView.as_view(), name='post_detail'),
  path('post/<int:pk>/', views.AllappDetailView.as_view(), name='post_detail'),
  path('app/new/', views.AllappCreateView.as_view(), name='post_new'),
]