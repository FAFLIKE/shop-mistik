from django.db import models

# Create your models here.
class Goods(models.Model):
    image =  models.CharField(max_length=500)
