from django.urls import path
from app.consumers import MyChatApp

websocket_urlpatterns = [
    path("ws/wsc/", MyChatApp.as_asgi())
]