from django.contrib import admin

from users.models import Profile
from vehicles.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'name', 'segment', 'manufacture_year', 'capacity', 'price']
    fields = ['brand', 'name', 'segment', 'manufacture_year', 'capacity', 'price', 'img', 'description']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'cash']
    fields = ['user', 'cash']
