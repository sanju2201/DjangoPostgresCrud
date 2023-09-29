from django.db import models

# Create your models here.
class Posiion(models.Model):
    title = models.CharField(max_length=50)

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    position = models.ForeignKey(Posiion, on_delete=models.CASCADE)