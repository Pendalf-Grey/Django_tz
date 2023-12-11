import uuid
from django import forms
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)


class Author(models.Model):
    author_name = models.CharField(max_length=255)


class Comic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)


class Rating(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    comic_id = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name='ratings')
    user_id = models.IntegerField(Comic)
    value = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 6)], widget=forms.Select)
