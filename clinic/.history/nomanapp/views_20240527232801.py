# views.py
from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment
from django.core.mail import send_mail
from .forms import QuoteForm
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
import stripe

from .forms import PaymentForm

stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    form = PaymentForm()
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            token = request.POST.get('stripeToken')
            try:
                charge = stripe.Charge.create(
                    amount=2450,  # Example amount in cents
                    currency='usd',
                    description='Dentacare Service',
                    source=token,
                )
                # Payment successful, set payment_success to True
                return render(request, 'home.html', {'form': form, 'payment_success': True})
            except stripe.error.CardError as e:
                # Card was declined
                error_message = e.error.message
                return render(request, 'home.html', {'form': form, 'error': error_message})
    return render(request, 'home.html', {'form': form})



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

# views.py


def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect to thank you page after successful submission
    else:
        form = AppointmentForm()
    return render(request, 'home.html', {'form': form})

# views.py (continued)
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


