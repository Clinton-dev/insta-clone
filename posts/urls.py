from django.urls import path
from .views import (
    PictureListView,
    PictureDetailView,
    PictureCreateView,
    PictureUpdateView,
    PictureDeleteView,
    UserPictureListView
)

from . import views

urlpatterns = [
    path('', PictureListView.as_view(), name='home'),
    path('search/', views.search_post, name='search'),
    path('user/<str:username>/posts', UserPictureListView.as_view(), name='user-posts'),
    path('picture/<int:pk>/', PictureDetailView.as_view(), name='post-detail'),
    path('picture/new/', PictureCreateView.as_view(), name='post-new'),
    path('picture/update/<int:pk>/', PictureUpdateView.as_view(), name='post-update'),
    path('picture/delete/<int:pk>/', PictureDeleteView.as_view(), name='post-delete'),
]