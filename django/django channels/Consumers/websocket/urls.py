from django import views
from django.urls import path
from websocket import views
urlpatterns = [
    path('<str:group>/',views.base)
]
