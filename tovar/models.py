from django.db import models

# Create your models here.
class modelGoods(models.Model):
    image = models.CharField(max_length=500)
    name =  models.CharField(max_length=100)
