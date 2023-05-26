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
    return redirect ("/")

def edit_profile(request):
    if 'id' in request.session:
        user = User.objects.get(id=request.session['id'])
        context = {
            'user': user
        }
        if request.method=="GET":
            return render (request, "edit_profile.html", context)
        if request.method=="POST":
            user.profile.display_name = request.POST['display_name']
            user.profile.bio = request.POST['bio']
            user.profile.country = request.POST['country']
            user.profile.city = request.POST['city']
            user.profile.profile_picture = request.FILES['profile_picture']
            user.profile.save()
            return redirect ('/profile')
    