from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Picture

def home(request):
    context = {
        "posts": Picture.objects.all()
    }
    return render(request,"posts/home.html", context)

def search_post(request):
    query = request.GET.get('query')
    if query != None:
        posts = Picture.objects.filter(name__contains=query)

    context = {
        'posts': posts,
        'title':'search posts'
    }

    return render(request, 'posts/search.html', context)

class PictureListView(LoginRequiredMixin, ListView):
    model= Picture
    template_name='posts/home.html' #<app-name>/<model>_<view-type>.html
    context_object_name='posts'
    ordering= ['-date_posted']

class UserPictureListView(ListView):
    model= Picture
    template_name='posts/user_posts.html' #<app-name>/<model>_<view-type>.html
    context_object_name='posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Picture.objects.filter(author=user).order_by('-date_posted')

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