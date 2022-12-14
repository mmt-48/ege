from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='home'),
 path('ege/', views.ege, name='ege'),
 path('index/', views.index, name='index'),
 path('probls/<int:pkkk>/', views.probls, name='probls'),
 path('task/<int:pkk>/', views.task, name='task'),
 path('theme/<int:pkk>/', views.theme, name='theme')
]
