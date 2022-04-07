from django.urls import path
from .consumsers import MyAsync,MyJsonAsync
websocket_urlpatterns = [
    path('async/',MyAsync.as_asgi()),
    path('Jsonasync/',MyJsonAsync.as_asgi())
]