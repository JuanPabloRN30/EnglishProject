from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class MyUser(models.Model):
    user_django = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.CharField(max_length=100, null = True)
    number_listening = models.BigIntegerField(default = 0)
    number_writing = models.BigIntegerField(default = 0)
    number_reading = models.BigIntegerField(default = 0)
    def __str__(self):
        return self.user.username

class Song(models.Model):
    url_video = models.CharField(max_length=500)
    letter = models.TextField()
    name = models.CharField(max_length=500)

class Option(models.Model):
    text = models.CharField(max_length=200)
    correct = models.NullBooleanField()
    song = models.ForeignKey(Song, on_delete = models.CASCADE)
