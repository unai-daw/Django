from audioop import reverse
from django.db import models


class Platerak(models.Model):
    izena = models.CharField(max_length=200)
    deskripzioa = models.TextField()
    prezioa = models.FloatField()
    FechaCreacion = models.DateField()

