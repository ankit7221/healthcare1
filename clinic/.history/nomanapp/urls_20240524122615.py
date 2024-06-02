# nomanapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/about', views.about, name='about'),
    path('doctors/', views.doctors, name='doctors'),
    path('blog/', views.blog, name='blog'),
    path('services/', views.services, name='services'),
    path('blog_single/', views.blog_single, name='blog_single'),
    path('contact/', views.contact, name='contact'),
  
]
