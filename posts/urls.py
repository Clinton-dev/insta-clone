from django.urls import path
from .views import (
    PictureListView,
    PictureDetailView,
    PictureCreateView,
    PictureUpdateView,
    PictureDeleteView
)

urlpatterns = [
    path('', PictureListView.as_view(), name='home'),
    path('picture/<int:pk>/', PictureDetailView.as_view(), name='post-detail'),
    path('picture/new/', PictureCreateView.as_view(), name='post-new'),
    path('picture/update/<int:pk>/', PictureUpdateView.as_view(), name='post-update'),
    path('picture/delete/<int:pk>/', PictureDeleteView.as_view(), name='post-delete'),
]