from django.views.generic import CreateView
from .models import Booking
from .forms import BookingForm


class AddBooking(CreateView):
    """
    Create a booking view
    """
    template_name = 'bookings/create_booking.html'
    model = Booking
    form_class = BookingForm
    success_url = '/lessons/our_classes'
    
    def form_valid(self, form):
        form.instance.client = self.request.user
        return super(AddBooking, self).form_valid(form)
