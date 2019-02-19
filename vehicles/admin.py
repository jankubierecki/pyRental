from django.contrib import admin

from vehicles.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'name', 'segment', 'manufacture_year', 'capacity', 'price']
    fields = ['brand', 'name', 'segment', 'manufacture_year', 'capacity', 'price']
