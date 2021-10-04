from posts.models import Post
from likes.permissions import hasSelflikedOrReadOnly
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, viewsets, status, permissions
from .models import Likes
from .serializers import LikeSerializer


class LikesViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, hasSelflikedOrReadOnly]

    def perform_create(self, serializer):
        post_instance = get_object_or_404(Post, pk=self.request.data['post'])

        # if user likes the post
        if self.request.data['like']:
            already_up_voted = Likes.objects.filter(post=post_instance, liked_by=self.request.user).exists()
            if already_up_voted:
                raise serializers.ValidationError({"message": "You have already liked this post"})
            else:
                serializer.save(liked_by=self.request.user, post=post_instance)
        # if dislikes
        else:
            already_down_voted = Likes.objects.filter(post=post_instance, disliked_by=self.request.user).exists()
            if already_down_voted:
                raise serializers.ValidationError({"message": "You have already disliked this post"})
            else:
                serializer.save(disliked_by=self.request.user, post=post_instance)
