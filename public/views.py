from django.shortcuts import render

# Views for public or anything starting with / url
# This will contain landing page, and general information about the site.

def landing(request):
    return render (request, "index.html")
