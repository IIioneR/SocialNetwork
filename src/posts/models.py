import datetime

from django.contrib.auth.models import User
from django.db import models

from TestTask import settings


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_profile')
    last_request = models.DateTimeField(null=True, blank=True)

    def update_last_request(self) -> None:
        self.last_request = datetime.datetime.now()
        self.save()


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='users')
    created_at = models.DateTimeField()
    last_updated_at = models.DateTimeField()
    content = models.TextField()


class Like(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='posts')
    liked_at = models.DateTimeField(null=True, blank=True)
    value = models.BooleanField(default=False)

    def update_is_liked(self, flag: bool) -> None:
        # Updates value and liked_at time
        self.value = flag
        self.liked_at = datetime.datetime.now()
        self.save()
