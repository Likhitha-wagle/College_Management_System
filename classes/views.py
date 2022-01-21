from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Classes
from .serializers import ClassesSerializer

# Create your views here.

class AddClasses(APIView):
    serializer_class=ClassesSerializer
    def post (self,request,format="json"):
        try:
            serializer=ClassesSerializer(data=request.data)
            classname=Classes.objects.filter(class_name=request.data['class_name']).exists() 
            if classname:
                return Response("Class name already exists",status=status.HTTP_409_CONFLICT)  
            else:    
                if serializer.is_valid():
                    serializer.save()
                return Response({"Status":"Class Created","Data":serializer.data},status=status.HTTP_201_CREATED)
        except:
            return Response("Invalid entry",status=status.HTTP_409_CONFLICT)
