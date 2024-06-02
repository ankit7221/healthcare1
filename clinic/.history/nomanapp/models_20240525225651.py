from django.db import models
from django.utils import timezone

#appointmnet model
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateTimeField(default=timezone.now)  # Provide a default value
    time = models.TimeField(default="00:00:00")       # Provide a default value
    message = models.TextField()

    def __str__(self):
        return self.name
    
#quote model
class Quote(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    Website=models.URLField(blank=True)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name
        
