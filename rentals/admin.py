from django.contrib import admin
from rentals.models import Rental


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ['car', 'profile', 'start_date', 'cost']
    fields = ['car', 'profile', 'cost', 'start_date', 'end_date', 'paid', 'additional_info']
    readonly_fields = ['cost']
