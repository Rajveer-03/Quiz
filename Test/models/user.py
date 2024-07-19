from django.db import models

class User(models.Model):
    Email = models.EmailField(max_length=200)
    Password = models.CharField(max_length=200)

    def __str__(self):
        return self.Email