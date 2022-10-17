from django.db import models

class Produktuak(models.Model):
  izena = models.CharField(max_length=255)
  prezioa = models.CharField(max_length=255)
  iraungipenData = models.DateField(max_length=255)
