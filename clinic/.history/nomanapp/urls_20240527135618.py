
from django.contrib import admin
from django.urls import path
from . import views
from .views import get_quote
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name="home"),
    path('contact.html',views.contact,name='contact'),
    path('about.html',views.about,name='about'),
    path('home.html', views.home, name='home'),
    path('services.html', views.services, name='services'),
    path('doctors.html', views.doctors, name='doctors'),
    path('blog.html', views.blog, name='blog'),
    path('blog-single.html', views.blog_single, name='blog_single'),
    path('make_appointment/', views.make_appointment, name='make_appointment'),
    path('thank_you/',views.thank_you,name='thank_you'),
    path('get-quote/', get_quote, name='get_quote'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
