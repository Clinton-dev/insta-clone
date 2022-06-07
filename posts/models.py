from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


class Picture(models.Model):
    name = models.CharField(null=False, max_length=50)
    # image = models.ImageField(null=False, blank=False)
    image = CloudinaryField('image')
    date_posted = models.DateTimeField(null=False, default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})