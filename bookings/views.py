from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Booking
from .forms import BookingForm
from django.shortcuts import render


class BookingsList(ListView):
    """
    View to see all bookings
    """
    template_name = 'bookings/manage_bookings.html'
    model = Booking
    context_object_name = 'bookings'

    # Ensures logged in users can only see their own bookings but staff can
    # see all bookings
    # Code from:
    # https://www.youtube.com/watch?v=q2GGBThrgmA&list=PL_6Ho1hjJirn8WbY4xfVUAlcn51E4cSbY&index=5
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(client=self.request.user)
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
