from django.db import models

# Create your models here.
class modelGoods(models.Model):
    image = models.URLField()
    name =  models.CharField(max_length=100)
    price =  models.CharField(max_length=12)
    discription = models.TextField()
