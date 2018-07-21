from django.test import TestCase
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
