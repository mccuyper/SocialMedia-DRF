from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status, permissions, serializers
from .models import Likes
from posts.views import Post
from .serializers import LikeSerializer
from .permissions import hasSelflikedOrReadOnly


class LikesViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, hasSelflikedOrReadOnly]
    def perform_create(self, serializer):
        post_instance = get_object_or_404(Post, pk=self.request.data['post'])
        if self.request.data['like']:
            liked = Likes.objects.filter(post=post_instance, liked_by=self.request.user).exists()

            if liked:
                raise serializers.ValidationError({'message': 'Post has been liked already by you!'})
            else:
                serializer.save(liked_by=self.request.user, post=post_instance)

        else:
            disliked = Likes.objects.filter(post=post_instance, disliked_by=self.request.user).exists()

            if disliked:
                raise serializers.ValidationError({'message': 'Post has been liked already by you!'})
            else:
                serializer.save(disliked_by=self.request.user, post=post_instance)
                
        return super().perform_create(serializer)