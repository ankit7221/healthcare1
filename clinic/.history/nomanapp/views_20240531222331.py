from django.shortcuts import render, redirect
from .forms import AppointmentForm, UserRegistrationForm, QuoteForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages  # Import messages from Django contrib
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Appointment, Product
import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponseRedirect
from django.views import View
from .models import Price
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView as AuthLoginView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView

stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def doctors(request):
    return render(request, 'doctors.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def services(request):
    return render(request, 'services.html', {})

def blog_single(request):
    return render(request, 'blog-single.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST.get('message-name', '')
        message_email = request.POST.get('message-email', '')
        message_subject = request.POST.get('message_subject', '')
        umessage = request.POST.get('umessage', '')

        send_mail(
            message_subject,
            umessage,
            message_email,
            ['ankitchoudhary2451@gmail.com']
        )

        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})

@login_required
def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user  # Associate the appointment with the logged-in user
            appointment.save()
            return redirect('thank_you')  # Redirect to thank you page after successful submission
    else:
        form = AppointmentForm()
    return render(request, 'home.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')

def get_quote(request):
    quote_form = QuoteForm()
    
    if request.method == 'POST':
        if 'quote_form_submit' in request.POST:
            quote_form = QuoteForm(request.POST)
            if quote_form.is_valid():
                quote_form.save()
                return redirect('thank_you')

    return render(request, 'home.html', {'quote_form': quote_form})

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Signup successful! You are now logged in.')
            return redirect('home')  # Ensure 'home' is the name of your homepage URL
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def profile(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'registration/profile.html', {'appointments': appointments})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        domain = "http://127.0.0.1:8000/success/"
        if settings.DEBUG:
            domain = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return redirect(checkout_session.url)

class SuccessView(TemplateView):
    template_name = "success.html"

class CancelView(TemplateView):
    template_name = "cancel.html"

class ProductLandingPageView(TemplateView):
    template_name = "landing.html"
 
    def get_context_data(self, **kwargs):
        product = Product.objects.get(name="Test Product")
        prices = Price.objects.filter(product=product)
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "prices": prices
        })
        return context

class LoginView(AuthLoginView):
    template_name = 'login.html'
    

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'