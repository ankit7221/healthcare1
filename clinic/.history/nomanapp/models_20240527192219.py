from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#appointmnet model
class Appointment(models.Model):
     DEPARTMENT_CHOICES = [
        ('Teeth Whitening', 'Teeth Whitening'),
        ('Teeth Cleaning', 'Teeth Cleaning'),
        ('Quality Brackets', 'Quality Brackets'),
        ('Modern Anesthetic', 'Modern Anesthetic'),
    ]
     user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)# Associate with user
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
        
