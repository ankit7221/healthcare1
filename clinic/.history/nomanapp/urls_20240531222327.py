from django.contrib import admin
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import profile
from nomanapp.views import (
    CreateCheckoutSessionView,
    SuccessView,
    CancelView,
    ProductLandingPageView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about'),
    path('home.html', views.home, name='home'),
    path('services.html', views.services, name='services'),
    path('doctors.html', views.doctors, name='doctors'),
    path('blog.html', views.blog, name='blog'),
    path('blog-single.html', views.blog_single, name='blog_single'),
    path('make_appointment/', views.make_appointment, name='make_appointment'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('get-quote/', views.get_quote, name='get_quote'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    
    path('cancel/', views.CancelView.as_view(), name='cancel'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('', views.ProductLandingPageView.as_view(), name='landing'),
]