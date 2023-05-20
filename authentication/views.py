from django.shortcuts import render
from .models import User

# Create your views here.

def login(request): # to handle both get and post
    if request.method == "GET":
        return render (request, 'login.html')

def register(request): # both get and post
    if request.method =="GET":
        return render (request, 'register.html')


