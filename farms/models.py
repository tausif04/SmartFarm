from django.db import models

class AgricultureFarm(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    moisture = models.FloatField()

class CattleFarm(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    water_level = models.FloatField()

class PoultryFarm(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    water_level = models.FloatField()
  
class Fisheries(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()