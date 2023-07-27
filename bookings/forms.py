from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Form to create a booking
    """
    class Meta:
        model = Booking
        fields = ['level', 'day', 'time']

        labels = {
            'level': 'Level',
            'day': 'Day',
            'time': 'Time'
        }
