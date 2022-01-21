from django.db import models
from classes.models import Classes

# Create your models here.
class Student(models.Model):
    student_name=models.CharField(max_length=200,unique=True)
    contact_number=models.CharField(max_length=12)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        primary_key=False,
    )
    classid=models.OneToOneField(
        Classes,
        on_delete=models.CASCADE,
        primary_key=False,
        unique=False,
    )
    # ForeignKey(Classes,on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        db_table = "student" 