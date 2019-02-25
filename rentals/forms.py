from django.contrib.admin import widgets
from django.forms import ModelForm
from django import forms

from rentals.models import Rental


class DateInput(forms.DateInput):
    input_type = 'date'


class RentalCreateForm(ModelForm):
    class Meta:
        model = Rental
        fields = ('start_date', 'end_date', 'additional_info',)
        exclude = ('profile', 'paid')
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }
