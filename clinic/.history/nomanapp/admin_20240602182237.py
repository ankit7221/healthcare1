# admin.py
from django.contrib import admin
from .models import Appointment,Quote


admin.site.register(Appointment)
admin.site.register(Quote)
