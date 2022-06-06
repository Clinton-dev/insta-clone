from django.urls import path
from .views import PictureListView, PictureDetailView

urlpatterns = [
    path('', PictureListView.as_view(), name='home'),
    path('picture/<int:pk>', PictureDetailView.as_view(), name='post-detail')
]