# from logging import raiseExceptions

from django.shortcuts import get_object_or_404, render , redirect
from requests import request


from .models import Student

from rest_framework.response import Response

from rest_framework.decorators import api_view

from .serializers import stu_Serializers

from rest_framework import status

from rest_framework.decorators import APIView



class CR(APIView):

    def post(self,request):
        f1=request.data

        f2=stu_Serializers(data=f1)
        
        if f2.is_valid(raise_exception=True):
            f2.save()

            return Response(
                f2.data
            )
        return Response(stu_Serializers.errors(), status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        f1=Student.objects.all()
        print(f1)
        f2=stu_Serializers(f1,many=True)

        return Response(
            f2.data
        )


class UD(APIView):

    def put(self,request,id):
        f1=Student.objects.get(id=id)
        f2=stu_Serializers(instance=f1 , data=request.data)

        f2.is_valid()
        f2.save()
        return Response(f2.data, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self,request,id):
        f1=Student.objects.get(id=id)
        f=request.data

        f2=stu_Serializers(instance=f1,data=f)

        if f2.is_valid():
            f2.save()
            return Response(f2.data)


    def delete(self,request,id):
        f1=get_object_or_404(Student , id=id)
        f1.delete()
        return Response('ITEM deleted sucessfully')



