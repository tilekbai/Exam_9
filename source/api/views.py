from rest_framework import generics

from .serializers import *


class AddToFavView(generics.CreateAPIView):
    serializer_class = AddToFavSerializer


class DeleteFavView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeleteFavSerializer
    queryset = Favorite.objects.all()