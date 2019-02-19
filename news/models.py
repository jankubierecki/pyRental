from django.db import models
from vehicles.models import Car


class Post(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField("Utworzono", auto_now_add=True)
    description = models.TextField("opis", max_length=255, null=True, blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.car.name, self.created_at)

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'newsy'
        ordering = ['created_at']
