from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import signup
from .serializers import Rserializers, Userializers
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# 1. ---> Serializers <----
# crud
# @csrf_exempt
# def apiID(request,id):
#     try:
#         detail = signup.objects.get(id=id)
#         se = Rserializers(detail)
#     except signup.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':    
#         return JsonResponse(se.data,safe=False)
    
#     elif request.method == 'DELETE':
#         detail.delete()
#         return JsonResponse(se.data,safe=False)

#     elif request.method == 'PUT':
        
#         dta = JSONParser().parse(request)
#         se = Rserializers(detail,data = dta)
#         if se.is_valid():
#             se.save()
#             return JsonResponse(se.data,safe=False)
#         else:
#             return JsonResponse(se.errors,safe=False)
    
# 2. ---> Request & Response <----
@api_view(['GET','DELETE','PUT'])
def apiID(request,id):
    try:
        detail = signup.objects.get(id=id)
        se = Rserializers(detail)
    except signup.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':    
        return Response(se.data)
    
    elif request.method == 'DELETE':
        detail.delete()
        return Response(se.data)

    elif request.method == 'PUT':
        se = Rserializers(detail, data = request.data)
        if se.is_valid():
            se.save()
            return Response(se.data)
        else:
            return Response(se.errors)  #no need to speicfy (safe=False)



# post or get data of models
@csrf_exempt
def api(request):
    if request.method == 'GET':
        details = signup.objects.all()
        RestDetails = Rserializers(details,many = True)
        return JsonResponse(RestDetails.data,safe=False)
    
    elif request.method == 'POST':
        DSerializer = JSONParser().parse(request)
        se = Rserializers(data =  DSerializer)
        if se.is_valid():
            se.save()
            return JsonResponse(se.data,safe=False)
        else:
            return JsonResponse(se.errors)


# user creation from request
@api_view(['GET','POST'])
def userapi(request):
    if request.method == 'GET':
        da = User.objects.all()
        RestDetails = Userializers(da,many = True)
        return Response(RestDetails.data)

    # there is no need for (JSONparser()) when using (request.data)
    elif request.method == 'POST':
        #without (request.data)
        # ud = JSONParser().parse(request)
        # us = Userializers(data = ud)

        # with (request.data)
        us = Userializers(data = request.data)
        if us.is_valid():
            us.save()
           # return JsonResponse(us.data,safe=False) # need to specify safe
            return Response(us.data)
        else:
            return Response(us.errors)
