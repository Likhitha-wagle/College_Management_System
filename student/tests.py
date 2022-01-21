import json
from django.test import TestCase
from rest_framework.test import APIClient,APITestCase
from django.urls import reverse
import json
from rest_framework import status
from django.contrib.auth.models import User
from student.models import Student
from classes.models import Classes

# Create your tests here.
class BaseTestCase(APITestCase):
    def setUp(self):
        self.client=APIClient()
        self.username='likhitha'
        self.email='likhitha@gmail.com'
        self.password='likhitha'

        self.admin=User.objects.create_superuser(self.username,self.email,self.password)
        self.client.force_authenticate(user=self.admin)

    def test_api(self):
        user=self.admin
        self.classes1=Classes.objects.create(class_name="five")
        self.classes1.save()
        self.student1=Student.objects.create(student_name="Seemitha",contact_number="1234567892",email="seemitha@gmail.com",classid=self.classes1)
        self.student1.save()
        record=Student.objects.get()
        self.assertEqual(record.student_name,"Seemitha")

    def test_post_api(self):
        user=self.admin
        classes1=Classes.objects.create(class_name="five")
        student2={"student_name":"Likhithaa","contact_number":"'1234567892","email":"Likhithaa@gmail.com","classid":classes1.id}
        response=self.client.post('http://127.0.0.1:8000/api/AddStudent',student2,follow=True)
        result=response.json()
        print(result)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_get_api(self):
        user=self.admin
        response=self.client.get('http://127.0.0.1:8000/api/ViewStudent',follow=True)
        result=response.json()
        print(result)
        self.assertEqual(response.status_code,status.HTTP_200_OK)