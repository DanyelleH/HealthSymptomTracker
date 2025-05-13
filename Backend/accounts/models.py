from django.db import models
from django.contrib.auth.models import AbstractUser
from symptoms.models import Symptoms
# Create your models here.
class User(AbstractUser):
    symptoms = models.ManyToManyField(Symptoms, related_name ="symptoms", blank=True)
    
    def __str__(self):
        return f"{self.username} ({self.first_name}, {self.last_name})"