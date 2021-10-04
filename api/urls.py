from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from posts.views import PostViewSet
from likes.views import LikesViewSet
router=DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'posts', PostViewSet)
router.register(r'likes', LikesViewSet)
urlpatterns=router.urls