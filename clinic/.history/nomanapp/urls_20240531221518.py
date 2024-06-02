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
    path('', include('nomanapp.urls')),
    path('', views.home, name="home"),
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
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('', ProductLandingPageView.as_view(), name='landing'),
]
