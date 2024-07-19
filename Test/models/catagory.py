from django.db import models

class Catagory(models.Model):
    Name = models.CharField()

    def __str__(self):
        return self.Name