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
        self.response = self.client.post(
            reverse("create"),
            self.jokecategory_data,
            format="json"
        )

    def test_api_can_create_a_joke_category(self):
        """Tests the API has the ability to create joke categories"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_joke_category(self):
        """Tests API can get a given joke category"""
        joke_category = JokeCategory.objects.get()
        response = self.client.get(
            reverse("details", kwargs={"pk": joke_category.id}), format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, joke_category)

    def test_api_can_update_joke_category(self):
        """Tests the API can update a given joke category"""
        updated_joke_category = {"name": "Different Joke Category"}
        joke_category = JokeCategory.objects.get()
        response = self.client.put(
            reverse("details", kwargs={"pk": joke_category.id}), updated_joke_category, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_joke_category(self):
        """Tests the API can delete a given joke category"""
        joke_category = JokeCategory.objects.get()
        response = self.client.delete(
            reverse("details", kwargs={"pk": joke_category.id}), format="json", follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
