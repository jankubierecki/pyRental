from django.contrib.auth.models import User
from django.db import models
from djmoney.models.fields import MoneyField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cash = MoneyField(max_digits=14, decimal_places=0, default_currency='PLN')

    def __str__(self):
        return '{0} {1}'.format(self.user.first_name, self.user.last_name)
