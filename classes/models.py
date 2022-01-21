from django.db import models

# Create your models here.

class Classes(models.Model):
    class_name=models.CharField(max_length=200)
    
    class Meta:
        db_table = "classes" 