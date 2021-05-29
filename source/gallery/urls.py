from os import name
from django.contrib import admin
from django.urls import path

from .views import *

app_name = "gallery"

urlpatterns = [
    # Photo
    
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', PhotoView.as_view(), name='view-photo'),
    path('create/photo/', CreatePhotoView.as_view(), name='add'),
    path('<int:pk>/update/photo/', PhotoUpdateView.as_view(), name='update-photo'),
    path('<int:pk>/delete/photo/', PhotoDeleteView.as_view(), name='delete'),

    # albom

    path('albom/<int:pk>/', AlbomView.as_view(), name='view-albom'),
    path('create/albom/', CreateAlbomView.as_view(), name='add-albom'),
    path('<int:pk>/update/albom/', AlbomUpdateView.as_view(), name='update-albom'),
    path('<int:pk>/delete/albom/', AlbomDeleteView.as_view(), name='delete-albom')
]
