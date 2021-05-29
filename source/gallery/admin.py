from django.contrib import admin
from .models import Photo, Albom

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'caption', 'albom', 'date', 'photo']
    list_filter = ['author']
    search_fields = ['author']
    fields = ['id', 'author', 'caption', 'albom', 'date']
    readonly_fields = ['id', 'date']


class AlbomAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'name', 'description', 'date']
    list_filter = ['author']
    search_fields = ['author']
    fields = ['id', 'author', 'name', 'description']
    readonly_fields = ['id', 'date']



admin.site.register(Photo, PhotoAdmin)
admin.site.register(Albom, AlbomAdmin)


