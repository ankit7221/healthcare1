from django.db import models
from django.utils import timezone


#appointmnet model
class Appointment(models.Model):
     DEPARTMENT_CHOICES = [
        ('Teeth Whitening', 'Teeth Whitening'),
        ('Teeth Cleaning', 'Teeth Cleaning'),
        ('Quality Brackets', 'Quality Brackets'),
        ('Modern Anesthetic', 'Modern Anesthetic'),
    ]
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
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_photos/', default='profile_photos/default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'