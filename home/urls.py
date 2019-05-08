
from django.urls import path
from . import views

urlpatterns = [

  path('', views.AppView.as_view(), name='index'),
  path('results/', views.SearchView.as_view(), name='search'),
  path('post/<int:pk>/', views.AppDetailView.as_view(), name='post_detail'),
  path('post/<int:pk>/', views.AppUpdateView.as_view(), name='post_detail'),
  path('app/new/', views.AppCreateView.as_view(), name='post_new'),
  path('request/new/', views.AllappCreateView.as_view(), name='apost_new'),
  path('post/<int:pk>/reqest', views.AllappDetailView.as_view(), name='apost_detail'),
  path('com/', views.ComCreateView.as_view(), name='com_new'),
  path('category/<category>/', views.CategoryView.as_view(), name='index_filter')
]