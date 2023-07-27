from django.urls import path
from .views import AddBooking


urlpatterns = [
    path('create_booking/', AddBooking.as_view(), name='create_booking')
]
