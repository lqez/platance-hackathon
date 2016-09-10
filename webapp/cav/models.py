from __future__ import unicode_literals

from django.db import models


class Rider(models.Model):
    name = models.CharField(max_length=255)
    level = models.IntegerField(default=1)


class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=10000)


class Order(models.Model):
    requestDate = models.DateField(db_index=True)
    requestTime = models.TimeField()

    deliveryTime = models.DateTimeField()
    deliveryCompleteTime = models.DateTimeField()

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    orderedMenus = models.ManyToManyField(Menu)
