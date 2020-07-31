from django.db import models


# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=12)
    city_code = models.CharField(max_length=6)
