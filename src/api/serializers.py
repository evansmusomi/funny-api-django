from rest_framework import serializers
from .models import JokeCategory


class JokeCategorySerializer(serializers.ModelSerializer):
    """Maps the model instance into a JSON object"""

    class Meta:
        """Maps serializer's fields to the model fields"""
        model = JokeCategory
        fields = ("id", "name", "date_created", "date_modified")
        read_only_fields = ("date_created", "date_modified")
