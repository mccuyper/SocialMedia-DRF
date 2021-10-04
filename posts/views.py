from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from .models import Post
from .serializers import PostSerializer
from users.permissions import IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                            IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)