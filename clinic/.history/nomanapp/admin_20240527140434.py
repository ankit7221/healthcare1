from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'date', 'time', 'department')
    list_filter = ('user', 'department')

admin.site.register(Appointment, AppointmentAdmin)