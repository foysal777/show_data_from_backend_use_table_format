from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    father_name = models.TextField(default='Null')
    
    def __str__(self) -> str:
       return f"Name: {self.name }  ,  Roll : { self.roll}"