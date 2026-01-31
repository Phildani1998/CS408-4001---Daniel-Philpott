from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):
    def test_home_page_returns_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_hello_world(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Hello World")