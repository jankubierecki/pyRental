import datetime

from django.db import models


class Car(models.Model):
    brand = models.CharField("Marka", max_length=255)
    name = models.CharField("Model", max_length=255)
    segment = models.CharField("Segment", max_length=255)
    manufacture_year = models.IntegerField("Rok produkcji", default=datetime.datetime.now().year)
    capacity = models.FloatField("Pojemność")
    price = models.FloatField("Cena")
    description = models.TextField("Opis", max_length=255, null=True, blank=True)
    img = models.ImageField("Zdjęcie", null=True, default='no-photo-car.jpg', upload_to='images/uploaded',
                            blank=True)

    def __str__(self):
        return "{0} {1}".format(self.name, self.brand)

    class Meta:
        verbose_name = 'Samochód'
        verbose_name_plural = 'Samochody'
        ordering = ['manufacture_year']
