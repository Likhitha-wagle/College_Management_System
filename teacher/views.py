from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from classes.models import Classes
from .models import Teacher
from .serializers import TeacherSerializer

# Create your views here.

class AddTeacher(APIView):
    serializer_class=TeacherSerializer
    def post (self,request,format="json"):
        # try:
            serializer=TeacherSerializer(data=request.data)
            # v=[]
            # for i in request.data['classid']:
            #     print(i)
            #     cls=Classes.objects.get(id=i)
            #     v.append(str(cls))
            # print(v)
            # request.data['classid']=v
            if serializer.is_valid():
                serializer.save()
            return Response({"Status":"Created"},status=status.HTTP_201_CREATED)
        # except:
        #     return Response("Invalid entry",status=status.HTTP_409_CONFLICT)

class TeacherView(APIView):
    serializer_class=TeacherSerializer
    def get(self,request,format='json'):
        try:
            query=Teacher.objects.all()
            serializer=TeacherSerializer(query,many=True)
            return Response({"Status":"OK","Data": serializer.data},status=status.HTTP_200_OK)
        except:
            return Response("Not Found",status=status.HTTP_403_FORBIDDEN)
