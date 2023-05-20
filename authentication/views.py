from django.shortcuts import render, redirect
from django.contrib import sessions
from .models import User
import bcrypt

# Create your views here.

def login(request): # to handle both get and post
    if request.method == "GET":
        return render (request, 'login.html')
    if request.method =="POST":
        form_username = request.POST['username']
        form_password = request.POST['password']
        if User.objects.filter(username= form_username):
            user = User.objects.get(username = form_username)
            stored = user.password
            if bcrypt.checkpw(form_password.encode(), stored.encode()):
                request.session['id'] = user.id
                return redirect ('/auth/success')
        return redirect('/auth/login')

def register(request): # both get and post
    if request.method =="GET":
        return render (request, 'register.html')
    if request.method =="POST":
        if User.objects.filter(username=request.POST['username']):
            return redirect ('/auth/register') # will be handled by manager later instead
        form_password = request.POST['password']
        hashed_password = bcrypt.hashpw(form_password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(username = request.POST['username'], password=hashed_password, email=request.POST['email'], phone=request.POST['phone'])
        request.session['id'] = user.id
        return redirect ('/auth/login')


def success(request): # to go away after testing login and registration completely
    if 'id' in request.session:
        return render (request, 'success.html')
    return redirect('/auth/login')


def logout(request):
    if 'id' in request.session:
        del request.session['id']    
    return redirect ('/auth/login')

