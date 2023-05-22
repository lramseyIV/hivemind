from django.contrib import admin
from .models import User, VerificationURL
# Register your models here.
admin.site.register(User)
admin.site.register(VerificationURL)
