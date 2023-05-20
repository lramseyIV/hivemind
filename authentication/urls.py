from django.urls import path
from . import views
# This urls is for auth only and is meant to handle all authentication related requests
# I don't like usign django built in authentication

urlpatterns = [
    path("login", views.login),
    path("register", views.register)
]