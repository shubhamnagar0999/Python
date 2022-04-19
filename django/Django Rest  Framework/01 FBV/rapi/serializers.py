from dataclasses import field
from pyexpat import model
from .models import signup
from django.contrib.auth.models import User
from rest_framework import serializers


# without Modalserializer 
# class Rserializers(serializers.Serializer):
#     user = serializers.CharField(max_length=20)
#     email = serializers.EmailField()
#     name = serializers.CharField(max_length=20)
#     lname = serializers.CharField(max_length=20)

#     # for save data in models
#     def create(self, validated_data):
#         return signup.objects.create(**validated_data)
    
#     #for update data in models both funtion auto call when save method is call
#     def update(self,detail,validate_data):
#         s = signup(**validate_data)
#         s.id = detail.id
#         s.save()
#         return s


# with ModalSerializer : there is no need to create creat() and update() function
class Rserializers(serializers.ModelSerializer):
    class Meta:
        model = signup
        fields = '__all__'




class Userializers(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    email= serializers.EmailField()
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)


