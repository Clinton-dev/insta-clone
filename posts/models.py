from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Picture(models.Model):
    name = models.CharField(null=False, max_length=50)
    image = models.ImageField(null=False, blank=False)
    date_posted = models.DateTimeField(null=False, default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)