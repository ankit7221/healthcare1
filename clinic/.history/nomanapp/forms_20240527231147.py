# forms.py
from django import forms
from .models import Appointment
from .models import Quote

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'date', 'time','department', 'message']
        
class QuoteForm(forms.ModelForm):
    class Meta:
        model=Quote
        fields= ['full_name','email','phone','message']        

class PaymentForm(forms.Form):
    stripeToken = forms.CharField(widget=forms.HiddenInput())
    amount = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.HiddenInput())