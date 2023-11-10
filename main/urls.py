from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='home'),
 path('ege/', views.ege, name='ege'),
 path('index/', views.index, name='index'),
 path('pdf/<int:e_tt>', views.pdf, name='pdf'),
 path('variant/<int:pkk><int:e_tt>/', views.variant, name='variant'),
 path('probls/<int:pkkk>/<int:mm>/<int:e_tt>/', views.probls, name='probls'),
 path('task/<int:pkk>/', views.task, name='task'),
 path('theme/<int:pkk>/', views.theme, name='theme')
]
