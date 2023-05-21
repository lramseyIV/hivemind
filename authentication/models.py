from django.db import models
import re
# My own user model
class UserManager(models.Manager):
    def auth_validator(self, request):
        errors = {}
        # ensure that email is the proper format
        email_pattern = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
        if not (re.search(email_pattern,request.POST['email'])):
            errors['email error'] = "Invalid Email Format."

        # ensure that passwords match
        if not request.POST['password'] == request.POST['confirm-password']:
            errors['password error'] = "Passwords do not match."

        # Ensure Password Strength
        password_pattern  = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-_=+{};:,<.>]).{8,}$'
        if not (re.search(password_pattern, request.POST['password'])):
            errors['password format error'] = "Password must be at least 8 characters with at least one capital letter, one number, and one special character."

        # Ensure phone consists of only numbers. Twilio functions will ensure number works later
        try:
            tel = int(request.POST['phone'])
        except ValueError:
            errors['phone error'] = "Phone number invalid format."
        
        return errors
        

class User (models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20) # For account creation, verification and MFA later
    objects = models.Manager()
    validator = UserManager()
    
