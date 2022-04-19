from rest_framework import serializers
from .models import Student,Forclassview

# class Student_Serializer(serializers.Serializer):
#     name = serializers.CharField(max_length=50)
#     lname = serializers.CharField(max_length=50)
#     phone = serializers.IntegerField()

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         s = Student(**validated_data)
#         s.id = instance.id
#         s.save()
#         return s


#serializer for function
class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


#serializer for class
class For_class(serializers.ModelSerializer):
    class Meta:
        model = Forclassview
        fields = "__all__"
    