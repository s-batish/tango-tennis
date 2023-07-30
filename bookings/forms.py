from django import forms
from .models import Booking
from django.core.exceptions import ValidationError
from datetime import datetime


# Class to create datepicker
# Code from
# https://nancylin.xyz/how-to-implement-date-time-picker-in-django-without-javascript/
class DatePickerInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    """
    Form to create a booking
    """
    class Meta:
        model = Booking
        fields = ['level', 'day', 'time']
        widgets = {
            'day': DatePickerInput(),
        }
        day = forms.DateField
        labels = {
            'level': 'Level',
            'day': 'Date',
            'time': 'Time'
        }

    def clean(self):
        level = self.cleaned_data['level']
        day = self.cleaned_data['day']
        time = self.cleaned_data['time']

        # Ensures class can only be booked for future dates
        if day < datetime.today().date():
            raise ValidationError(
                'Invalid date - please choose a future date')

        # If a class at that level, date and time has been booked, raise an
        # error
        if Booking.objects.filter(level=level, day=day, time=time).exists():
            raise ValidationError(
                f"Sorry this {level} class has already been booked"
            )
