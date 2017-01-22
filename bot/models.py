from django.db import models

# Create your models here.
class Query(models.Model):
    concept = models.CharField(max_length=250)
    city = models.CharField(max_length=250, default="montreal")

class Result(models.Model):
    location_x = models.FloatField()
    location_y = models.FloatField(git )
