from django.test import TestCase
from .models import Review


class TestViews(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 400)
        self.assertTemplateUsed(response, 'home/index.html')


class TestRedirectViews(TestCase):
    
    def test_add_review(self):
        response = self.client.get('/add_review/')
        self.assertEqual(response.status_code, 302)
