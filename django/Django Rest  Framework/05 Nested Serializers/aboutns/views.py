from django.shortcuts import render
from rest_framework import generics
from .models import Student,Teacher
from .serializers import Sserializer,Tserializer
# Create your views here.


class CBVStudents(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Sserializer

class CBVTeacher(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = Tserializer

