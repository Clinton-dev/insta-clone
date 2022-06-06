from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Picture

def home(request):
    context = {
        "posts": Picture.objects.all()
    }
    return render(request,"posts/home.html", context)

class PictureListView(ListView):
    model= Picture
    template_name='posts/home.html' #<app-name>/<model>_<view-type>.html
    context_object_name='posts'
    ordering= ['-date_posted']

class PictureDetailView(DetailView):
    model= Picture