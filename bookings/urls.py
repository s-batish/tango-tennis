from django.urls import path
from .views import AddBooking, BookingsList, DeleteBooking, EditBooking


urlpatterns = [
    path('create_booking/', AddBooking.as_view(), name='create_booking'),
    path('manage_bookings/', BookingsList.as_view(), name='manage_bookings'),
    path('delete_booking/<slug:pk>/', DeleteBooking.as_view(),
         name='delete_booking'),
    path('edit_booking/<slug:pk>/', EditBooking.as_view(),
         name='edit_booking')
]
