from django.urls import path
from . import views
# This urls is for auth only and is meant to handle all authentication related requests
# I don't like usign django built in authentication

urlpatterns = [
    path("login", views.login),
    path("register", views.register),
    path('verify', views.verify),
    path('logout', views.logout),
    path('confirm/<str:url_string>', views.confirm_account),
    path('sendpw', views.forgot_password)
]