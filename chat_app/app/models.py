from django.db import models
from django.conf import settings

# Create your models here.

# Post Model
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="posts_liked", blank=True)
    
    def __str__(self):
        return self.user.username