from django.db import models


class Sooyusil(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    longt = models.DecimalField(max_digits=30, decimal_places=20)
    langt = models.DecimalField(max_digits=30, decimal_places=20)
    call = models.CharField(max_length=100)
