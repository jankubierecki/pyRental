import datetime

from django.contrib.admin import widgets
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms

from rentals.models import Rental
from vehicles.models import Car


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

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.car = kwargs.pop('car', None)
        super(RentalCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(RentalCreateForm, self).clean()

        try:
            car = Car.objects.get(pk=self.car)
        except Exception:
            raise ValidationError('Ten samochód jest chwilowo niedostępny')
        profile = self.user.profile
        if car.price > profile.cash:
            self.add_error(None, ValidationError('Brak środków na koncie.'))

        current_date = datetime.date.today()
        start_date = self.cleaned_data.get('start_date')
        if start_date is None:
            start_date = current_date
        if start_date < current_date:
            raise ValidationError('Nieprawidłowa data.')
        end_date = self.cleaned_data.get('end_date')
        if start_date > end_date:
            raise ValidationError('Data zwrotu musi być większa.')

        return cleaned_data
