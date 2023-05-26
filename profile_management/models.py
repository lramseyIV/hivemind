from django.db import models

# Create your models here.


class Profile(models.Model):
    display_name = models.CharField(max_length=255, default="changeme")
    bio = models.TextField(default="I have not edited my bio yet.")
    country = models.CharField(default="here", max_length=100)
    city = models.CharField(default="here city", max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
