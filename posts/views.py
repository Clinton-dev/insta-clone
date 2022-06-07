from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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

class PictureDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= Picture
    success_url= '/'

    def test_func(self):
        picture = self.get_object()
        if self.request.user ==  picture.author:
            return True
        return False

class PictureCreateView(LoginRequiredMixin,CreateView):
    model= Picture
    fields = ['name', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PictureUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model= Picture
    fields = ['name', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        picture = self.get_object()
        if self.request.user ==  picture.author:
            return True
        return False