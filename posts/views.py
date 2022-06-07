from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
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

class PictureCreateView(LoginRequiredMixin,CreateView):
    model= Picture
    fields = ['name', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PictureUpdateView(LoginRequiredMixin, UpdateView):
    model= Picture
    fields = ['name', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)