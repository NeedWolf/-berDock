
from django.urls import path
from . import views

urlpatterns = [

  path('', views.AppView.as_view(), name='index'),
  path('results/', views.SearchView.as_view(), name='search'),
  path('post/<int:pk>/', views.AppDetailView.as_view(), name='post_detail'),
  path('post/<int:pk>/', views.AppUpdateView.as_view(), name='post_edit'),
  path('app/new/', views.AppCreateView.as_view(), name='post_new'),
]