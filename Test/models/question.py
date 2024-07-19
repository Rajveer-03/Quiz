from django.db import models
from .test import Test

class Question(models.Model):
    Test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="test")
    Question = models.CharField(max_length=1000)
    Marks = models.IntegerField()
    img_Solution = models.ImageField(upload_to='Assests/Solutions/', null=True, blank=True)
    text_Solution = models.TextField(null=True, blank=True)

    def __str__(self) :
        return self.Question