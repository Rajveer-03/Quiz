from django.db import models
from .student import Student
from .question import Question
from .answer import Answer
from .test import Test

class Student_Attempt(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Test = models.ForeignKey(Test, on_delete=models.CASCADE)
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
