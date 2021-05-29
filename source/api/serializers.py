from rest_framework import serializers
from gallery.models import Favorite


class AddToFavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"

 
class DeleteFavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"