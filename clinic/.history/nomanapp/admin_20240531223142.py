# admin.py
from django.contrib import admin
from .models import Appointment
from .models import Product, Price

admin.site.register(Appointment)

class PriceInlineAdmin(admin.TabularInline):
    model = Price
    extra = 0
 
 
class ProductAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin]
 
 
admin.site.register(Product, ProductAdmin)