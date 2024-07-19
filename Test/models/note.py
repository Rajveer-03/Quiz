from django.db import models
from .catagory import Catagory

class Notes(models.Model):
    Catagory = models.ForeignKey(Catagory, null=True, default=None, on_delete=models.CASCADE)
    Title = models.CharField()
    document = models.FileField(upload_to='Assests/Notes/',)

    def __str__(self):
        return self.Title
    

    @staticmethod
    def notes_by_catagory(ids):
        c_id = Catagory.objects.get(id=ids)
        return Notes.objects.filter(Catagory = c_id).order_by('-id')