from django.db import models
from email.message import Message


class Contact(models.Model):
    Name= models.CharField(max_length=50)
    Email=models.EmailField(max_length=30)
    Subject=models.CharField(max_length=30)
    Message=models.TextField()


class Employee(models.Model):
    emp_name = models.CharField(max_length=50,null=False,blank=False)
    emp_salary  = models.IntegerField(null=False,blank=False)
# Create your models here.
