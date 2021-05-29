from django.urls import path

from .views import *

app_name = 'api_v1'

urlpatterns = [
    path('add/', AddToFavView.as_view(), name='add-api'),
    path('remove/<int:pk>/', DeleteFavView.as_view(), name='add-api'),
]
