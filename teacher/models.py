from django.db import models
from classes.models import Classes

# Create your models here.

class Teacher(models.Model):
    teacher_name=models.CharField(max_length=200)
    contact_number=models.CharField(max_length=12)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    classid=models.CharField(max_length=500,blank=True,null=True,default='')

    class Meta:
        db_table = "teacher" 