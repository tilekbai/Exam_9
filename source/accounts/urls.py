from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/profile/', UserDetailView.as_view(), name='user-detail'),
]