import imp
from django.shortcuts import render
from .models import Picture

"""
    posts = [
    {
        "caption":"new cat video",
        "likes": "5",
        "comments": "5",
        "time_posted":"13hours",
        "author": "clint-dev"
    },
    {
        "caption":"new cat video",
        "likes": "5",
        "comments": "5",
        "time_posted":"13hours",
        "author": "clint-dev"
    },
    ]
"""

def home(request):
    context = {
        "posts": Picture.objects.all()
    }
    return render(request,"posts/home.html", context)