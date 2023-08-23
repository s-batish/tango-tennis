from django.test import TestCase
from .models import Lessons
from django.contrib.auth.models import User
from datetime import date


class TestViews(TestCase):

    # Test Our Classes page renders correctly
    def test_our_classes_page(self):
        response = self.client.get('/lessons/our_classes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/our_classes.html')

    # Test cases for creating lessons
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="bob",
            password="password123"
        )

    # Test for making a booking
    def test_add_lesson_page(self):
        self.client.login(username="bob", password="password123")
        response = self.client.get('/lessons/add_lesson/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lessons/add_lessons.html')


class TestRedirectViews(TestCase):
    # Tests when a user is not logged in

    def test_add_lesson(self):
        response = self.client.get('/lessons/add_lesson/')
        self.assertEqual(response.status_code, 302)

    def test_edit_lesson(self):
        response = self.client.get('/lessons/edit_lesson/1/')
        self.assertEqual(response.status_code, 302)

    def test_delete_lesson(self):
        response = self.client.get('/lessons/delete_lesson/1/')
        self.assertEqual(response.status_code, 302)
