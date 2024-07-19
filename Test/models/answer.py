from django.db import models
from .question import Question

class Answer(models.Model):
    Question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question")
    Answer = models.CharField(max_length=100)
    is_Correct = models.BooleanField(default=False)

    def __str__(self) :
        return self.Answer