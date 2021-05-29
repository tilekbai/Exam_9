from django.contrib import admin
from django.urls import path

from .views import *

app_name = "gallery"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
]
