from django.urls import path
from . import views


urlpatterns = [
 path('', views.index, name='home'),
 path('index/', views.index, name='index'),
 path('probls/<int:pkk>/', views.probls, name='probls'),
 path('task/<int:pkk>/', views.task, name='task')
]
