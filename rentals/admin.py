from django.contrib import admin
from rentals.models import Rental


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ['car', 'profile', 'start_date', 'price']
    fields = ['car', 'profile', 'price', 'start_date', 'end_date', 'paid', 'additional_info']
    readonly_fields = ['price']
