from django.test import TestCase
from .models import Booking
from django.contrib.auth.models import User
from datetime import date


class TestViews(TestCase):

    # Test cases for making a booking for a logged in user
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="bob",
            password="password123"
        )
        self.booking = Booking(
            client=self.user,
            level="beginner",
            day=date.today,
            time=1
        )

    # Test for making a booking
    def test_add_booking_page(self):
        self.client.login(username="bob", password="password123")
        response = self.client.get('/bookings/create_booking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/create_booking.html')

    # Test for managing bookings
    def test_manage_bookings_page(self):
        self.client.login(username="bob", password="password123")
        response = self.client.get('/bookings/manage_bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/manage_bookings.html')


class TestRedirectViews(TestCase):
    # Tests when a user is not logged in

    def test_add_booking(self):
        response = self.client.get('/bookings/create_booking/')
        self.assertEqual(response.status_code, 302)

    def test_edit_booking(self):
        response = self.client.get('/bookings/edit_booking/1/')
        self.assertEqual(response.status_code, 302)

    def test_delete_booking(self):
        response = self.client.get('/bookings/delete_booking/1/')
        self.assertEqual(response.status_code, 302)
