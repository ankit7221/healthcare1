# models.py
from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
