from dataclasses import field
from rest_framework import serializers
from .models import Data

class Dserialzier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data 
        fields = ['url','name','lname']