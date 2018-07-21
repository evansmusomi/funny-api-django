from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import JokeCategory


class ModelTestCase(TestCase):
    """Defines the JokeCategory model test suite"""

    def setUp(self):
        """Defines the test client and variables"""
        self.jokecategory_name = "Short Quotes"
        self.jokecategory = JokeCategory(name=self.jokecategory_name)

    def test_model_can_create_a_joke_category(self):
        """Tests the JokeCategory model can create a Joke Category"""
        initial_count = JokeCategory.objects.count()
        self.jokecategory.save()
        new_count = JokeCategory.objects.count()
        self.assertNotEqual(initial_count, new_count)


class ViewTestCase(TestCase):
    """Defines API views test suite"""

    def setUp(self):
        """Defines the test client and variables"""
        self.client = APIClient()
        self.jokecategory_data = {"name": "Funny Lazy Quotes"}

    def test_api_can_create_a_joke_category(self):
        """Tests the API has the ability to create joke categories"""
        self.response = self.client.post(
            reverse("create"),
            self.jokecategory_data,
            format="json"
        )
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
