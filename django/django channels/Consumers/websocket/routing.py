#like urls.py

from django.urls import path
from .consumers import MyAsync,MySync

websocket_urlpatterns = [
    path('async/<str:groupname>', MyAsync.as_asgi()),
    path('sync', MySync.as_asgi()),
]
