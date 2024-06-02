from django.db import models
from django.utils import timezone
from django.conf import settings


#appointmnet model
class Appointment(models.Model):
     DEPARTMENT_CHOICES = [
        ('Teeth Whitening', 'Teeth Whitening'),
        ('Teeth Cleaning', 'Teeth Cleaning'),
        ('Quality Brackets', 'Quality Brackets'),
        ('Modern Anesthetic', 'Modern Anesthetic'),
    ]
     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)  
     name = models.CharField(max_length=100)
     email = models.EmailField()
     date = models.DateTimeField(default=timezone.now)  # Provide a default value
     time = models.TimeField(default="00:00:00")       # Provide a default value
   
     department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES,default='Teeth Whitening')
     message = models.TextField()
     def __str__(self):
         return self.name
    
#quote model
class Quote(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    stripe_product_id = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name    
        
class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)  # cents
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)