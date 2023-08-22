from django.test import TestCase
from .models import Review
from django.contrib.auth.models import User
from datetime import date


class TestViews(TestCase):

    # Tests home page renders correctly
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    # Test cases for leaving a review for a logged in user
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="bob",
            password="password123"
        )
        self.review = Review(
            user=self.user,
            name="Bob",
            body="Great class",
            created_on=date.today
        )
        self.review.save()

    # Test for adding a review
    def test_add_review_page(self):
        self.client.login(username="bob", password="password123")
        response = self.client.get('/add_review/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/add_review.html')

    # Test for editing a review
    def test_edit_review_page(self):
        self.client.login(username="bob", password="password123")
        response = self.client.get('/edit_review/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/edit_review.html')

    # Test for deleting a review
    def test_delete_review_page(self):
        self.client.login(username="bob", password="password123")
        response = self.client.get('/delete_review/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/review_confirm_delete.html')

    # Test for managing review
    def test_manage_reviews_page(self):
        self.client.login(username="bob", password="password123")
        response = self.client.get('/my_reviews/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/my_reviews.html')


class TestRedirectViews(TestCase):
    # Tests when a user is not logged in

    def test_add_review(self):
        response = self.client.get('/add_review/')
        self.assertEqual(response.status_code, 302)

    def test_edit_review(self):
        response = self.client.get('/edit_review/1/')
        self.assertEqual(response.status_code, 302)

    def test_delete_review(self):
        response = self.client.get('/delete_review/1/')
        self.assertEqual(response.status_code, 302)
