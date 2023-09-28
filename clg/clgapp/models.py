from django import forms
from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Branch(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Purpose(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Student(models.Model):
    name = models.CharField(max_length=100)
    DOB = models.DateField()
    age = models.IntegerField()
    email = models.EmailField(blank=True)
    phone=models.IntegerField(null=True)
    gender = models.CharField(max_length=1)
    materials=models.CharField(blank=True,max_length=50)
    address = models.TextField(max_length=50,blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    purpose=models.ForeignKey(Purpose,on_delete=models.CASCADE)

    def __str__(self):
        return self.name




