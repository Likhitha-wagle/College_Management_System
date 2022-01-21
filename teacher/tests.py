import json
from django.test import TestCase
from rest_framework.test import APIClient,APITestCase
from django.urls import reverse
import json
from rest_framework import status
from django.contrib.auth.models import User
from teacher.models import Teacher

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
        self.teacher1=Teacher.objects.create(teacher_name="Seemitha",contact_number="1234567892",email="seemitha@gmail.com",classid="[1,2]")
        self.teacher1.save()
        record=Teacher.objects.get()
        self.assertEqual(record.teacher_name,"Seemitha")

    def test_post_api(self):
        user=self.admin
        teacher2={"teacher_name":"Seemitha","contact_number":"'1234567892","email":"seemitha@gmail.com","classid":"[1,2]"}
        response=self.client.post('http://127.0.0.1:8000/api/AddTeacher',teacher2,follow=True)
        result=response.json()
        print(result)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_get_api(self):
        user=self.admin
        response=self.client.get('http://127.0.0.1:8000/api/ViewTeacher',follow=True)
        result=response.json()
        print(result)
        self.assertEqual(response.status_code,status.HTTP_200_OK)