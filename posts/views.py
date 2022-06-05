from django.shortcuts import render
from .models import Picture

def home(request):
    context = {
        "posts": Picture.objects.all()
    }
    return render(request,"posts/home.html", context)