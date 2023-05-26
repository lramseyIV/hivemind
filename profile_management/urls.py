from django.urls import path

from . import views
urlpatterns = [
    path("", views.profile_home),
    path("edit", views.edit_profile)
]

