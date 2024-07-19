from django.db import models
from .test import Test
from .student import Student

class Result(models.Model):
    Test = models.ForeignKey(Test, on_delete=models.CASCADE)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Rank = models.PositiveIntegerField(null=True)
    Total_Marks = models.IntegerField()
    Obtained_Marks = models.IntegerField(null=True)
    Total_Attempted = models.PositiveIntegerField()
    Accuracy = models.FloatField()
    Percentile = models.FloatField(null=True)
