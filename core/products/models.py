from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50),
    price = models.FloatField(max_length=50),
    #description = models.TextField(null = True, blank = True)
    
    
    def __str__(self):
        return self.name
    
