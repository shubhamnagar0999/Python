
from unicodedata import name
from RForm import views
from django.urls import path

urlpatterns = [
    path('Registration/',views.registration),
    path('SaveRegistration/',views.registration,name='SaveRegistration'),
]
