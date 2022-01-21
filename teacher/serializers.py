from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    classid=serializers.ListField()
    class Meta:
        model=Teacher
        fields="__all__"