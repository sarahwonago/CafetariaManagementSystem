from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Custom User Model with role attribute added.
    """
    
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('admin', 'Cafetaria Admin'),
    ]

    role = models.CharField(max_length=250, choices=ROLE_CHOICES, default='customer')
