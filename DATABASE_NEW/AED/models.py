from django.db import models


class AED(models.Model):
    address = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    manager = models.CharField(max_length=200)
    longt = models.DecimalField(max_digits=30, decimal_places=20)
    langt = models.DecimalField(max_digits=30, decimal_places=20)
    call = models.CharField(max_length=100)
