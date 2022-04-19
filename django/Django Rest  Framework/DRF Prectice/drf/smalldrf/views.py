from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import Student,Forclassview
from django.views.decorators.csrf import csrf_exempt
from .serializers import Student_Serializer,For_class


from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import mixins,generics

# Create your views here.

#function based view
@csrf_exempt
def home(request):
    if request.method == "GET":
        data = Student.objects.all()
        sdata = Student_Serializer(data,many=True)
        return JsonResponse(sdata.data,safe=False)

    if request.method == "POST":
        data = JSONParser().parse(request)
        sdata = Student_Serializer(data=data)
        if sdata.is_valid():
            sdata.save()
            return JsonResponse(sdata.data,safe=False)

        return HttpResponse("done")

@csrf_exempt
@api_view(['GET','DELETE','PUT'])
def d_u(request,id):
    try:
        ddata = Student.objects.get(id=id)
        sdata = Student_Serializer(ddata)
        
    except Student.DoesNotExist  :
        return HttpResponse("NOT FOUND")
    if request.method == "GET":
        return JsonResponse(sdata.data,safe=False)
    if request.method == "DELETE":
        data.delete()
        return HttpResponse("deleted")
    if request.method == "PUT":
        # data = JSONParser().parse(request)
        sdata = Student_Serializer(ddata,data=request.data)
        if sdata.is_valid():
            sdata.save()
            return HttpResponse("updated")
        else:
            return HttpResponse("ERROR")


#class based view

class stud(APIView):
    def get(self,request):
        data = Forclassview.objects.all()
        sdata = For_class(data,many=True)
        return Response(sdata.data)
      
    def post(self,request):
        sdata = For_class(data=request.data)
        if sdata.is_valid():
            sdata.save()
            return Response("saved")
        return HttpResponse("error")

class studpk(APIView):
    def getobject(self,id):
        try:
            data = Forclassview.objects.get(id=id)
            return data
        except Forclassview.DoesNotExist:
            return JsonResponse("NOT FOUND",safe=False)

    def get(self,request,id):
        data = self.getobject(id)
        if data is not None:
            sdata = For_class(data)
            return Response(sdata.data)
        else:
            return JsonResponse("NOT FOUND")

    def delete(self,request,id):
        data = self.getobject(id)
        data.delete()
        return Response("Deleted")

    def put(self,request,id):
        da = self.getobject(id)
        sdata = For_class(da,data = request.data)
        if sdata.is_valid():
            sdata.save()
            return Response("Updated")

#mixins and generics 
class M_and_G(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Forclassview.objects.all()
    serializer_class = For_class

    def get(self,request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class M_and_G_pk(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset = Forclassview.objects.all()
    serializer_class = For_class

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)

    def put(self,request,pk):
        return update(request,pk)



#Generics

class Generic(generics.ListCreateAPIView):
    queryset = Forclassview.objects.all()
    serializer_class = For_class

class Generic_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Forclassview.objects.all()
    serializer_class = For_class
    
