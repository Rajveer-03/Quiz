from django.db import models
from .user import User


class Student(models.Model):
    Email = models.ForeignKey(User, on_delete=models.CASCADE)
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    Gender = models.CharField(max_length=8, null=True)
    Age = models.IntegerField()
    Contact = models.CharField(max_length=15)
    Country = models.CharField(max_length=30, null=True)
    State = models.CharField(max_length=50, null=True)
    City = models.CharField(max_length=30, null=True)
    Address = models.CharField(max_length=130, null=True)

    def __str__(self):
        return self.Fname