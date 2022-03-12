import imp

from django import views
from . import views
from django.urls import path

urlpatterns = [
    
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
]