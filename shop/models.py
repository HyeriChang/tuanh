from django.db import models
from ckeditor.fields import RichTextField



# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    picture = models.ImageField()
    size = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    rating = models.FloatField()
    is_male = models.BooleanField()
    is_female = models.BooleanField()
    detail = RichTextField()