import imp
from os import stat
from django.http import JsonResponse, response
from django.shortcuts import render
from numpy import delete
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from CBVApp.serializers import Rserializer
from rest_framework import status
from .models import Data
# Create your views here.


class CBC(APIView):
    def get(self,request):
        da = Data.objects.all()
        serializer = Rserializer(da,many=True)
        return Response(serializer.data)

    def post(self,request):
        da = Rserializer(data = request.data)
        if da.is_valid():
            da.save()
        return Response('Saved')

class CBCpk(APIView):
    def getDetails(self,pk):
        try:
            return Data.objects.get(pk = pk)
        except Data.DoesNotExist:
            return JsonResponse('not found',safe=False)

    def get(self,request,pk):
        d = self.getDetails(pk)
        serial = Rserializer(d)
        return Response(serial.data)

    def delete(self,request,pk):
        d = self.getDetails(pk)
        d.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        d = self.getDetails(pk)
        s = Rserializer(d,data = request.data)
        if s.is_valid():
            s.save()
            return Response(status=status.HTTP_201_CREATED)
        