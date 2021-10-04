from .models import Likes
from rest_framework import serializers


class LikeSerializer(serializers.ModelSerializer):
    like = serializers.ReadOnlyField(source="liked_by.username")
    dislike = serializers.ReadOnlyField(source="disliked_by.username")

    class Meta:
        model = Likes
        fields = ("id", "post", "like", "dislike")
