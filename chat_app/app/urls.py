from django.urls import path
from app import views

urlpatterns = [
    path("post/", views.UserPost, name='post'),
]
