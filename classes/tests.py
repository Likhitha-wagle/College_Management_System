import json
from django.test import TestCase
from rest_framework.test import APIClient,APITestCase
from django.urls import reverse
import json
from rest_framework import status
from django.contrib.auth.models import User
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
        self.classes1=Classes.objects.create(class_name="four")
        self.classes1.save()
        record=Classes.objects.get()
        self.assertEqual(record.class_name,"four")

    def test_post_api(self):
        user=self.admin
        classes2={"class_name":"five"}
        response=self.client.post('http://127.0.0.1:8000/api/AddClasses',classes2,follow=True)
        result=response.json()
        print(result)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)