from django.shortcuts import render, redirect
from django.contrib import sessions
from authentication.models import User

# Views for profile management

def profile_home(request):
    if 'id' in request.session:
        user = User.objects.get(id=request.session['id'])
        context = {
            'user': user
        }
        return render (request, "profile_home.html", context)
