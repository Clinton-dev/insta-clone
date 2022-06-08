from django.test import TestCase

from django.test import TestCase

from .models import Picture
from django.contrib.auth.models import User


class PhotoTest(TestCase):
    def setUp(self):
        self.user = User()
        self.user.username = 'john doe'
        self.user.email = 'john@doe.com'
        self.user.save()

    def test_fields(self):
        photo = Picture()
        photo.name = 'foo bar'
        photo.image = 'foobar.jpg'
        photo.author_id = self.user.id
        photo.save()

        record = Picture.objects.get(pk=1)
        self.assertAlmostEquals(record, photo)



