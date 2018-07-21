from rest_framework import generics
from .serializers import JokeCategorySerializer
from .models import JokeCategory


class CreateView(generics.ListCreateAPIView):
    """Defines the create behaviour of our rest API"""
    queryset = JokeCategory.objects.all()
    serializer_class = JokeCategorySerializer

    def perform_create(self, serializer):
        """Saves the post data when creating a new joke category"""
        serializer.save()
