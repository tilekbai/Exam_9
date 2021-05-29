from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import BLANK_CHOICE_DASH

User = get_user_model()
# Create your models here.

class Photo(models.Model):
    photo = models.ImageField(blank=False)
    caption = models.CharField(max_length=155, blank=False)
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    albom = models.ForeignKey("gallery.Albom", blank=True, null=True, on_delete=models.CASCADE)


class Albom(models.Model):
    name = models.CharField(max_length=155, blank=False)
    description = models.TextField(max_length=555, blank=True)
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)