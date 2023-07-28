from django.urls import path
from .views import AddBooking, BookingsList


urlpatterns = [
    path('create_booking/', AddBooking.as_view(), name='create_booking'),
    path('manage_bookings/', BookingsList.as_view(), name='manage_bookings')
]
