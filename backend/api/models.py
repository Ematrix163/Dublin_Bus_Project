# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Currentweather(models.Model):
    dt = models.IntegerField(blank=True, null=True)
    dt_iso = models.DateTimeField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    temp = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    temp_min = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    temp_max = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pressure = models.IntegerField(blank=True, null=True)
    humidity = models.IntegerField(blank=True, null=True)
    wind_speed = models.IntegerField(blank=True, null=True)
    wind_deg = models.IntegerField(blank=True, null=True)
    rain_1h = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rain_3h = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rain_24h = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rain_today = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    snow_1h = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    snow_3h = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    snow_24h = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    snow_today = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    clouds_all = models.IntegerField(blank=True, null=True)
    weather_id = models.IntegerField(blank=True, null=True)
    weather_main = models.CharField(max_length=50, blank=True, null=True)
    weather_description = models.CharField(max_length=80, blank=True, null=True)
    weather_icon = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currentWeather'


class Holidays(models.Model):
    date = models.DateTimeField(primary_key=True)
    type = models.CharField(max_length=15, blank=True, null=True)
    timestamp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'holidays'


class Leavetimes(models.Model):
    dayofservice = models.DateTimeField(primary_key=True)
    tripid = models.IntegerField()
    progrnumber = models.SmallIntegerField()
    stoppointid = models.SmallIntegerField(blank=True, null=True)
    plannedtime_arr = models.IntegerField(blank=True, null=True)
    plannedtime_dep = models.IntegerField(blank=True, null=True)
    actualtime_arr = models.IntegerField(blank=True, null=True)
    actualtime_dep = models.IntegerField(blank=True, null=True)
    suppressed = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leavetimes'
        unique_together = (('dayofservice', 'tripid', 'progrnumber'),)


class Routes(models.Model):
    routes = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'routes'


class RoutesStopid(models.Model):
    busroute = models.CharField(primary_key=True, max_length=15)
    stopid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'routes_stopid'
        unique_together = (('busroute', 'stopid'),)


class Stopsstatic(models.Model):
    index = models.IntegerField(blank=True, null=True)
    stop_id = models.CharField(primary_key=True, max_length=12)
    stop_name = models.CharField(max_length=100, blank=True, null=True)
    stop_lat = models.DecimalField(max_digits=25, decimal_places=20, blank=True, null=True)
    stop_long = models.DecimalField(max_digits=25, decimal_places=20, blank=True, null=True)
    true_stop_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stopsStatic'


class Trips(models.Model):
    dayofservice = models.DateTimeField(primary_key=True)
    tripid = models.IntegerField()
    lineid = models.CharField(max_length=10, blank=True, null=True)
    routeid = models.CharField(max_length=20, blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    plannedtime_arr = models.IntegerField(blank=True, null=True)
    plannedtime_dep = models.IntegerField(blank=True, null=True)
    actualtime_arr = models.IntegerField(blank=True, null=True)
    actualtime_dep = models.IntegerField(blank=True, null=True)
    supressed = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trips'
        unique_together = (('dayofservice', 'tripid'),)
