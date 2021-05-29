from os import name
from django.contrib import admin
from django.urls import path

from .views import *

app_name = "gallery"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', PhotoView.as_view(), name='view-photo'),
    path('create/photo/', CreatePhotoView.as_view(), name='add'),
    path('<int:pk>/update/photo/', PhotoUpdateView.as_view(), name='update-photo'),
]
