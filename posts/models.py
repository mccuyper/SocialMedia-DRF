from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'