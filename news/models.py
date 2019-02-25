from django.db import models
from vehicles.models import Car


class Post(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.car.name, self.created_at)
