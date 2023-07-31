from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class EditBooking(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View to edit a booked class
    """
    template_name = 'bookings/create_booking.html'
    model = Booking
    form_class = BookingForm
    success_url = '/bookings/manage_bookings/'

    # Allows staff to edit any booked lessons but logged in users can only
    # edit their own
    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            return self.request.user == self.get_object().client


class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View to delete booked classes
    """
    model = Booking
    success_url = '/bookings/manage_bookings/'

    # Allows staff to delete any booked lessons but logged in users can only
    # delete their own
    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            return self.request.user == self.get_object().client
