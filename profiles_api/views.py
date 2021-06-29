from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serualizes


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serualizes.HelloSerializer

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
