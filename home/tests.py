from django.test import TestCase
from .models import Review


class TestViews(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 400)
        self.assertTemplateUsed(response, 'home/index.html')


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