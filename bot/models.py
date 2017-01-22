from django.db import models

# Create your models here.
class Query(models.Model):
    concept = models.CharField(max_length=250)
    location_x = models.FloatField()
    location_y = models.FloatField()
