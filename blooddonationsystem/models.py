from django.db import models
from  django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField()
    contactnumber=models.IntegerField()
    message=models.TextField()

    def __str__(self):
        return self.name


class Donor(models.Model):
    firstname=models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    gender=models.CharField(max_length=10)
    email=models.EmailField()
    contactno=models.IntegerField()
    DOB=models.DateField()
    major=models.CharField(max_length=100)
    Age=models.CharField(max_length=100)
    bloodgroup=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100)
    Address=models.TextField()

    def __str__(self):
        template = '{0.firstname} {0.lastname}'
        return template.format(self)


class Needblood(models.Model):
    firstname=models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    gender=models.CharField(max_length=10)
    email=models.EmailField()
    contactno=models.IntegerField()
    DOB=models.DateField()
    major=models.CharField(max_length=100)

    bloodgroup=models.CharField(max_length=100)

    def __str__(self):
        template = '{0.firstname} {0.lastname}'
        return template.format(self)
