from dataclasses import field
from django.db import DatabaseError
from rest_framework import serializers
from .models import Data
class Rserializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = "__all__"