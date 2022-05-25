from operator import mod
from .models import Student

from django.db.models import fields

from rest_framework import serializers

class stu_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('__all__')
    
# class studentserializer(serializers.ModelSerializer):
#     class Meta:
#         model=St_user

#         fields=('__all__')

