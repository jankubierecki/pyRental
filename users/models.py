from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cash = models.FloatField(default=0)

    def __str__(self):
        return f'{self.user.first_name, self.user.last_name} Profil'


