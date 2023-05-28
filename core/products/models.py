from django.db import models

# Create your models here.


class Category


class Product(models.Model):
    name = models.CharField(max_length=255, unique = True)
    price = models.FloatField()
    description = models.TextField(blank = True, null = True)
    #image = models.ImageField(upload_to = 'images/', blank = True, null = True)
    
    
    def __str__(self):
        return self.name
    

