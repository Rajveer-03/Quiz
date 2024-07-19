from django.db import models
from .catagory import Catagory

class Test(models.Model):
    Catagory = models.ForeignKey(Catagory, null=True, default=None, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30, unique=True)
    Timing = models.PositiveIntegerField()
    num_Questions = models.PositiveIntegerField()
    Total_Marks = models.PositiveIntegerField()

    def __str__(self) :
        return self.Name
    
    @staticmethod
    def test_by_catagory(ids):
        c_id = Catagory.objects.get(id=ids)
        return Test.objects.filter(Catagory = c_id).order_by('-id')
        