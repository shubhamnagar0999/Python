import imp
from django.urls import path
from mini import views
urlpatterns = [
    path('',views.index),
    path('home/',views.first)
]
