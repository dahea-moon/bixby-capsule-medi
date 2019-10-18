from django.db import models


class Sooyusil(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    longt = models.FloatField()
    langt = models.FloatField()
    call = models.CharField(max_length=100)