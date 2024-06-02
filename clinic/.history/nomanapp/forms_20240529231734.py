# forms.py
from django import forms
from .models import Appointment
from .models import Quote
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'date', 'time','department', 'message']
        
class QuoteForm(forms.ModelForm):
    class Meta:
        model=Quote
        fields= ['full_name','email','phone','message']        

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    
    class Meta:
        model= User
        fields=['username','email','password1','password1']
