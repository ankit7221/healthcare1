# forms.py
from django import forms
from .models import Appointment
from .models import Quote

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'date', 'time', 'message']
        
class Quoteform(forms.ModelForm):
    class Meta:
        model=Quote
        fields= ['full_name','email','phone','website','message']        
