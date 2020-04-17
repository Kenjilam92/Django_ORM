from django.db import models

class Wizard(models.Model):
    name = models.CharField(max_length=45)
    house = models.CharField(max_length=45)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()
    date_adopt= models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'Name: {self.name}'
    
# Create your models here.
