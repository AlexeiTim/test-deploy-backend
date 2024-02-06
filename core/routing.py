# chat/routing.py
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('socket.io/', consumers.app),
    path('ws/', consumers.YourConsumer.as_asgi())
]
