from django import views
from django.urls import path
from .views import CBC,CBCpk
urlpatterns = [
    path('',CBC.as_view()),
    path('<int:pk>',CBCpk.as_view())
]
