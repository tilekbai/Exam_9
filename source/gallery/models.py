from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Photo(models.Model):
    photo = models.ImageField(blank=False)
    caption = models.CharField(max_length=155, blank=False)
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name="photos")
    albom = models.ForeignKey("gallery.Albom", blank=True, null=True, on_delete=models.CASCADE, related_name="photos")
    private = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)



class Albom(models.Model):
    name = models.CharField(max_length=155, blank=False)
    description = models.TextField(max_length=555, blank=True)
    author = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name="alboms")
    private = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)


class Favorite(models.Model):
    author = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name="favorites")
    photo = models.ForeignKey("gallery.Photo", blank=True, null=True, on_delete=models.CASCADE)
    albom = models.ForeignKey("gallery.Albom", blank=True, null=True, on_delete=models.CASCADE)