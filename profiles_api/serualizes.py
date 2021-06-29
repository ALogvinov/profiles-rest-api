from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Серализатор для теста"""
    name = serializers.CharField(max_length=10)
