from django.db import models
from django.conf import settings

# Create your models here.

# Post Model
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="posts_liked", blank=True)
    
    class Meta:
        ordering = ('created', )
    
    def __str__(self):
        return self.user.username
    
    @property
    def like_count(self):
        try:
            like_count = self.liked_by.count()
        except:
            like_count = ''
        return like_count
            
            
class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('created', )