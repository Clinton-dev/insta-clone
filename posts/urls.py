from django.urls import path
from .views import PictureListView
from . import views

urlpatterns = [
    path('', PictureListView.as_view(), name='home')
]