from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Booking
from .forms import BookingForm
from django.shortcuts import render
from datetime import timedelta, date


class BookingsList(ListView):
    """
    View to see all bookings
    """
    template_name = 'bookings/manage_bookings.html'
    model = Booking
    context_object_name = 'bookings'

    # Ensures staff can see all bookings with a date greater than yesterday
    # but logged in users can only see their own bookings with a date greater
    # than yesterday
    def get_queryset(self):
        if self.request.user.is_staff:
            booking_list = Booking.objects.filter(
                day__gt=(date.today()-timedelta(days=1)))
            return booking_list
        else:
            booking_list = Booking.objects.filter(
                client=self.request.user,
                day__gt=(date.today()-timedelta(days=1)))
            return booking_list


class AddBooking(LoginRequiredMixin, CreateView):
    """
    Create a booking view
    """
    template_name = 'bookings/create_booking.html'
    model = Booking
    form_class = BookingForm
    success_url = '/bookings/manage_bookings/'

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super(AddBooking, self).form_valid(form)
