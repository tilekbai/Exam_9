from django.contrib import admin
from .models import Photo, Albom, Favorite

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'caption', 'albom', 'date', 'photo', 'private']
    list_filter = ['author']
    search_fields = ['author']
    fields = ['id', 'author', 'caption', 'albom', 'date', 'photo', 'private']
    readonly_fields = ['id', 'date']


class AlbomAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'name', 'description', 'date']
    list_filter = ['author']
    search_fields = ['author']
    fields = ['id', 'author', 'name', 'description']
    readonly_fields = ['id', 'date']


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['id', 'author','albom', 'photo']
    list_filter = ['id']
    search_fields = ['id']
    fields = ['id', 'author', 'albom', 'photo']
    readonly_fields = ['id']



admin.site.register(Photo, PhotoAdmin)
admin.site.register(Albom, AlbomAdmin)
admin.site.register(Favorite, FavoriteAdmin)


