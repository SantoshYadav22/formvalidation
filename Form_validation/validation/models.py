from django.db import models

# Create your models here.
class Model(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.IntegerField()
    Email=models.EmailField(max_length=100)
    Place=models.CharField(max_length=100)

def __str__(self):    
    return self.Name
