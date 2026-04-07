from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    
    USER_CHOICES = (
        ('owner','Owner'),
        ('player','Player')

    )

    user_type= models.CharField(max_length=10, choices=USER_CHOICES, default='player')
