from django.urls import path
from app import views

urlpatterns = [
    
    # post url
    path("post/", views.UserPost, name='post'),
    path("post/like/", views.LikePost, name='post-like'),
    path("delete-post/<int:id>", views.deletePost, name='delete-post'),
    path("post/comments/<int:id>", views.PostComments, name="post-comment"),
    
    # profile url
    path("profile/<str:username>", views.UserProfile, name="user-profile"),
]
