from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import mixins,generics
from .models import Data
from .serializers import Rserializer

# Create your views here.


#Mixins and generics class when using both
'''
Generics class : GenericAPIView class provide hadler methods : get(),post(),put(),delete

mixins classes : all classes has mixins methods
                 1. ListModelMixin     : provide list of data in models with action method list()
                 2. CreateModelMixin   : Add data to the models with action method create()
                 3. RetrieveModelMixin : To get data with primary key with action method retrive()
                 2. UpdateModelMixin   : To update data with the action method update()
                 2. DestroyModelMixin  : To delete data with action method destroy()
'''
'''        
class CBV(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Data.objects.all()
    serializer_class = Rserializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)


class CBVPk(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset = Data.objects.all()
    serializer_class = Rserializer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)
'''


#generic classes
'''
1. ListApiView : class provides functionality to use both [generics.GenericAPIView and mixins.ListModelMixin] with single class

2. CreateApiView : class provides functionality to use both [generics.GenericAPIView and mixins.CreateModelMixin] with single class

3. RetrieveApiView : class provides functionality to use both [generics.GenericAPIView and mixins.RetrieveModelMixin] with single class

4. UpdateApiView : class provides functionality to use both [generics.GenericAPIView and mixins.UpdateModelMixin] with single class

5. DestroyApiView : class provides functionality to use both [generics.GenericAPIView and mixins.destroyModelMixin] with single class

6. ListCreateApiView : class provides functionality to use [generics.GenericAPIView,mixins.ListModelmixin and mixins.createModelMixin] with single class

7. RestrieveUpdateDestroyApiView : class provides functionality to use [generics.GenericAPIView,mixins.DestroyModelMixin,mixins.RetrieveModelmixin and mixins.UpdateModelMixin] with single class

8. RetrieveDestroyApiView : class provides functionality to use [generics.GenericAPIView,mixins.RetrieveModelmixin and mixins.DestroyeModelMixin] with single class

9. RetrieveUpdateApiView : class provides functionality to use [generics.GenericAPIView,mixins.RetrieveModelmixin and mixins.UpdateModelMixin] with single class

'''
class CBV(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = Rserializer



class CBVPk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = Rserializer

 