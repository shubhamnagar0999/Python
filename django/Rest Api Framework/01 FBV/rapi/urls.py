import imp
from django import  views
from django.urls import path
from  rapi import views

urlpatterns = [
    path('',views.api),
    path('<int:id>',views.apiID),
    path('user/',views.userapi)
]
