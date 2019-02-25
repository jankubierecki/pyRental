import datetime
from django.db import models
from djmoney.models.fields import MoneyField


class Car(models.Model):
    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    segment = models.CharField(max_length=255)
    manufacture_year = models.IntegerField(default=datetime.datetime.now().year)
    capacity = models.FloatField()
    price = MoneyField(max_digits=14, decimal_places=0, default_currency='PLN')
    description = models.TextField(max_length=255, null=True, blank=True)
    img = models.ImageField(null=True, default='no-photo-car.jpg', upload_to='images/uploaded',
                            blank=True)

    def __str__(self):
        return "{0} {1}".format(self.name, self.brand)
