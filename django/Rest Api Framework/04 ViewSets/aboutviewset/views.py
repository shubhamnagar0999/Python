from asyncio.base_subprocess import ReadSubprocessPipeProto
from http.client import ResponseNotReady
from pstats import Stats
from django.http import JsonResponse
from pandas import reset_option
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.views import APIView
from rest_framework import status

from aboutviewset.serializers import Rserializers
from .models import Data
# Create your views here.

#viewset : do not need to create seprate urls for the key based operations and without key based operations
'''
class CBV(ViewSet):
    def create(self,request):
        se = Rserializers(data = request.data)
        if se.is_valid():
            se.save()
            return Response(status=status.HTTP_201_CREATED)


    def list(self,request):
        Da = Data.objects.all()
        serial = Rserializers(Da,many=True)
        return Response(serial.data)

    def retrieve(self,request,pk):
        try:
            da = Data.objects.get(pk = pk)
        except Data.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        serial = Rserializers(da)
        return Response(serial.data)

    def update(self,request,pk):
        try:
            da = Data.objects.get(pk = pk)
        except Data.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        serial = Rserializers(da,request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):
        try:
            da = Data.objects.get(pk = pk)
            da.delete()
        except Data.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
class CBV(ModelViewSet):   
    queryset = Data.objects.all()
    serializer_class = Rserializers
