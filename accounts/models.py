from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dietary_preferences = models.TextField(null=True, blank=True)
    dietary_restrictions = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username
