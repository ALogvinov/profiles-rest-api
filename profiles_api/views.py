from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request):
        """Вовзращает списко APIView"""
        an_apiview = ["Uses HTTP methods as function", "Is similar to a tradition Django view"]
        return Response({'message': 'ok', 'an_apiview': an_apiview})

    def post(self, request):
        """Тестовое сообщение пост"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Тестируем обновление"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Тестируем частичное обновление объекта"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Тестируем удаление объекта"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return Hello message"""
        an_apiview = ["Uses HTTP methods as function", "Is similar to a tradition Django view"]
        return Response({'message': 'ok', 'an_apiview': an_apiview})

    def create(self, request):
        """Create new Hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Тест получения метода по id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Тест получения метода update по id"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Тест получения метода partial_update по id"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Тест получения метода partial_update по id"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updatin profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """Handle create user auth token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating reading and updating profile feed item"""
    serializer_class = serializers.ProfileFeedItemSerializer
    authentication_classes = (TokenAuthentication,)
    serializers = (serializers.ProfileFeedItemSerializer,)
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """Set user profile to log user"""
        serializer.save(user_profile=self.request.user)
