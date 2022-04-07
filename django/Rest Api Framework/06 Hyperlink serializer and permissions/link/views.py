from multiprocessing import AuthenticationError
from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from link.models import Data
from link.serializers import Dserialzier

#permission classes : two types of authetication sesion and basic authentications
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

# Create your views here.
class CBV(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    queryset = Data.objects.all()
    serializer_class = Dserialzier