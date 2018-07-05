from django.db import models

# Create your models here.
class Weather(models.Model):
    weather_main = models.CharField(max_length=30)
    dt = models.DurationField(max_length=30)
    temp = models.IntegerField