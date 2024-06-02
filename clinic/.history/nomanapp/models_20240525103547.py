from django.db import models
from django.utils import timezone


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateTimeField(default=timezone.now)  # Provide a default value
    time = models.TimeField(default="00:00:00")       # Provide a default value
    message = models.TextField()

    def __str__(self):
        return self.name
