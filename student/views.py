from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from classes.models import Classes
from .models import Student
from .serializers import StudentSerializer

# Create your views here.

class AddStudent(APIView):
    serializer_class=StudentSerializer
    def post (self,request,format="json"):
        try:
            cls=Classes.objects.get(id=request.data['classid'])
            request.data['classid']=cls
            data=Student.objects.create(student_name=request.data['student_name'],contact_number=request.data['contact_number'],email=request.data['email'],classid=request.data['classid'])
            return Response({"Status":"Created"},status=status.HTTP_201_CREATED)
        except:
            return Response("Duplicate entry",status=status.HTTP_409_CONFLICT)

class StudentView(APIView):
    serializer_class=StudentSerializer
    def get(self,request,format='json'):
        try:
            query=Student.objects.all()
            serializer=StudentSerializer(query,many=True)
            return Response({"Status":"OK","Data": serializer.data},status=status.HTTP_200_OK)
        except:
            return Response("Not Found",status=status.HTTP_403_FORBIDDEN)
