import json
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from channels import Group
from .settings import MSG_TYPE_MESSAGE

@python_2_unicode_compatible
class MyUser(models.Model):
    user_django = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.CharField(max_length=100, null = True)
    number_listening = models.BigIntegerField(default = 0)
    number_writing = models.BigIntegerField(default = 0)
    number_reading = models.BigIntegerField(default = 0)
    def __str__(self):
        return self.user.username

@python_2_unicode_compatible
class Song(models.Model):
    url_video = models.CharField(max_length=500)
    letter = models.TextField()
    name = models.CharField(max_length=500)
    artist = models.CharField(max_length=100, default = "")
    duration = models.CharField(max_length=100, default = "")
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class OptionSong(models.Model):
    text = models.CharField(max_length=200)
    correct = models.NullBooleanField()
    song = models.ForeignKey(Song, on_delete = models.CASCADE)
    def __str__(self):
        return "Option from: " + self.song.name

@python_2_unicode_compatible
class Lecture(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    def __str__(self):
        return str(self.pk)

class OptionLecture(models.Model):
    text = models.CharField(max_length=200)
    correct = models.NullBooleanField()
    lecture = models.ForeignKey(Lecture, on_delete = models.CASCADE)
    def __str__(self):
        return "Option from: " + self.lecture.title

@python_2_unicode_compatible
class Room(models.Model):
    """
    A room for people to chat in.
    """
    # Room title
    title = models.CharField(max_length=255)
    # If only "staff" users are allowed (is_staff on django's User)
    staff_only = models.BooleanField(default=False)
    def __str__(self):
        return self.title

    @property
    def websocket_group(self):
        """
        Returns the Channels Group that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return Group("room-%s" % self.id)

    def send_message(self, message, user, msg_type=MSG_TYPE_MESSAGE):
        """
        Called to send a message to the room on behalf of a user.
        """
        final_msg = {'room': str(self.id), 'message': message, 'username': user.username, 'msg_type': msg_type}

        # Send out the message to everyone in the room
        self.websocket_group.send(
            {"text": json.dumps(final_msg)}
        )
