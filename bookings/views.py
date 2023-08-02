from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Booking
from .forms import BookingForm
from datetime import timedelta, date
from django.contrib import messages


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

    # Generates success message for successful booking of a class
    def form_valid(self, form):
        form.instance.client = self.request.user
        messages.add_message(
            self.request, messages.SUCCESS, 'Your class has been booked!')
        return super(AddBooking, self).form_valid(form)


class EditBooking(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View to edit a booked class
    """
    template_name = 'bookings/edit_booking.html'
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

    # Checks if class is already booked, then gives success message if not
    def form_valid(self, form):
        level = form.cleaned_data['level']
        day = form.cleaned_data['day']
        time = form.cleaned_data['time']
        if not Booking.objects.filter(
         level=level, day=day, time=time).exists():
            messages.success(self.request, 'Your class has been updated!')
        return super().form_valid(form)


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

    # Generates success message for successful deletion of class
    # Code from:
    # https://stackoverflow.com/questions/47636968/django-messages-for-a-successfully-delete-add-or-edit-item
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Your class has been deleted.')
        return super(DeleteBooking, self).delete(request, *args, **kwargs)
