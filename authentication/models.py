from django.db import models

# My own user model

class User (models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20) # For account creation, verification and MFA later
    
