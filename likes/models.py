from django.db import models
from posts.models import Post
from django.contrib.auth.models import User


class Likes(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User, related_name="like", on_delete=models.CASCADE, default=None, blank=True, null=True)
    disliked_by = models.ForeignKey(User, related_name="dislike", on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.post.title}'
