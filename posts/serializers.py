from rest_framework import serializers
from .models import Post
from likes.serializers import LikeSerializer


class PostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("id", "title", "content", "date_posted", "likes")
