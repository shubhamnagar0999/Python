from pickletools import read_long1
from struct import Struct
from .models import Student ,Teacher
from rest_framework import serializers

class Sserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class Tserializer(serializers.ModelSerializer):
    studends = Sserializer(many=True,read_only=True) 
    class Meta:
        model = Teacher
        fields = '__all__'





