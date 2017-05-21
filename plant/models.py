from django.db import models

# Create your models here.
class Type(models.Model):
    t_name = models.CharField(max_length=250)
    t_img = models.CharField(max_length=1000)
    t_description = models.CharField(max_length=1000)

class Plant(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=200)
    p_img = models.CharField(max_length=200)
    p_description = models.CharField(max_length=1000)
    p_quantity = models.IntegerField()

