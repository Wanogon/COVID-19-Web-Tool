from django.urls import path
from . import views
#import sys
#sys.path.append('D:\django_web\mysite\myapp')
#import views

urlpatterns = [
    path('templates/index.html/', views.index, name='index'),
    path('welcome.html/', views.welcome, name='welcome'),
    path('result.html/', views.result, name = 'result'),
    path('demo_wait.html/', views.demo_wait, name = 'demo_wait'),
]