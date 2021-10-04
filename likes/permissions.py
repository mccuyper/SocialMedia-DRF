from rest_framework import permissions


class hasSelflikedOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if self.request.method in permissions.SAFE_METHODS:
            return True
        return obj.liked_by==request.user or obj.disliked_by==request.user