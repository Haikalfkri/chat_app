from django.urls import path
from app import views

urlpatterns = [
    
    # post url
    path("post/", views.UserPost, name='post'),
    path("post/like/", views.LikePost, name='post-like'),
    path("delete-post/<int:id>", views.deletePost, name='delete-post'),
    path("post/comments/<int:id>", views.PostComments, name="post-comment"),
    
    # profile url
    path("profile/", views.Profile, name="user-profile"),
    path("profile/change_password/", views.PasswordsChangeView.as_view(template_name="app/user/change_password.html"), name="change-password"),
    
    # list of user
    path("members/", views.Members, name="member"),
    
    #chat
    path("chat/<str:username>", views.chatPage, name="chat"),
]
