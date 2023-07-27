from django import forms
from .models import Booking
from django.core.exceptions import ValidationError


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

        if Booking.objects.filter(level=level, day=day, time=time).exists():
            # if a time on that day is booked raise validation error
            raise ValidationError(
                f"Sorry this {level} class has already been booked"
            )
