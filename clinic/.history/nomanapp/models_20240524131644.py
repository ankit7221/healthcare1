# models.py
from django.db import models

class Appointment(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()

    def __str__(self):
        return self.full_name
