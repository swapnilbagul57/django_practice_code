from django.db import models

# Create your models here.
from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class Info(models.Model):
  firsname = models.CharField(max_length=250)
  lastname = models.CharField(max_length=250)
  address = models.CharField(max_length=255)
  city = models.CharField(max_length=200)
  mobile_no = models.CharField(max_length=12)
