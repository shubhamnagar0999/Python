from rest_framework import serializers
from .models import Data
class Rserializers(serializers.ModelSerializer):
    class Meta: 
        model = Data
        fields = ['name','lname']