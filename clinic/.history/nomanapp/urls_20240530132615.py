from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import profile

urlpatterns = [
    # Existing URL patterns
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
    path('profile/', profile, name='profile'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),  # Admin URL

    # Password reset URLs
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
