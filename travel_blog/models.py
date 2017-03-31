from django.db import models

# Create your models here.
class Regions(models.Model):
    region_name = models.CharField(max_length=200)
    update_date = models.DateTimeField('last updated date')

class Countries(models.Model):
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    country_name = models.CharField(max_length=200)
    update_date = models.DateTimeField('last updated date')
    #votes = models.IntegerField(default=0)
