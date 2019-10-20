from django.db import models


class Sooyusil(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    longt = models.CharField(max_length=100)
    langt = models.CharField(max_length=100)
    call = models.CharField(max_length=100)