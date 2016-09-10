from __future__ import unicode_literals

from django.db import models


class Rider(models.Model):
    name = models.CharField(max_length=255)
    level = models.IntegerField(default=1)

    def __unicode__(self):
        return unicode(self.name)


class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=10000)

    def __unicode__(self):
        return unicode(self.name)


class DeliveryTime(models.Model):
    time = models.TimeField()

    def __unicode__(self):
        return unicode(self.time.strftime('%H:%M'))


class Order(models.Model):
    requestDate = models.DateField(db_index=True)
    requestTime = models.TimeField()

    deliveryTime = models.DateTimeField()
    deliveryCompleteTime = models.DateTimeField()

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    address = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)


class MenuOrder(models.Model):
    menu = models.ForeignKey(Menu)
    count = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
