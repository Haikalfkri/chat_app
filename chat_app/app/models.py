from django.db import models
from django.conf import settings
from authentication.models import CustomUser

# Create your models here.

# Profile Model
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField()
    image = models.ImageField(upload_to="profile_images/")
    
    def __str__(self):
        return self.user.username
    
    @property
    def profileImageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        
        return url


# Post Model
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
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
            

# Comment Model
class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('created', )
        
    def __str__(self):
        return self.body
    
