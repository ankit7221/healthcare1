# models.py
from django.db import models
from django.utils import timezone

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateTimeField(default=timezone.now)
    time = models.TimeField()
    message = models.TextField()

    def __str__(self):
        return self.name
