import datetime

from django.contrib.auth.models import User
from django.db import models
from users.models import Profile
from vehicles.models import Car


class Rental(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField(verbose_name='Data Rozpoczęcia', default=datetime.date.today, editable=True)
    end_date = models.DateField(verbose_name='Data Zakończenia')
    paid = models.BooleanField(default=False)
    additional_info = models.TextField(verbose_name='Uwagi', max_length=255, null=True, blank=True)

    def __str__(self):
        return '{0} {1} {2} {3}'.format(self.profile.user.first_name, self.profile.user.last_name, self.car.brand,
                                        self.car.name)

    @property
    def price(self):
        return self.car.price

    class Meta:
        verbose_name = 'Zamówienie'
