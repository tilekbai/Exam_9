from django import forms

from .models import Photo, Albom

 
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('caption', 'author', 'photo', 'albom')


class AlbomForm(forms.ModelForm):
    class Meta:
        model = Albom
        fields = "__all__"


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')
