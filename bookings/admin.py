from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'level',
        'day',
        'time'
    )
    list_filter = ('level', 'day')
