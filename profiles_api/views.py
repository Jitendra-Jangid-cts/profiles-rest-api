from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns features"""
        an_apiview = [
            'User HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to urls',
        ]

        return Response ({'message': 'Hello !', 'An API View is here': an_apiview})

    def post(self, request):
        """Create a hello message with name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Update an object"""
        return Response ({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Partial Update"""
        return Response ({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete"""
        return Response ({'method': 'DELETE'})


class HellowViewSet(viewsets.ViewSet):
    """Test viewsets"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_ViewSet = [
            'Uses',
            'Automatically',
            'Provides',
        ]
        return Response({'message': 'Hey !', 'a_viewset': a_ViewSet})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} !'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handlde getting object by Id"""
        return Response ({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handlde updating object by Id"""
        return Response ({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handlde partial updating object by Id"""
        return Response ({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handlde deleting object by Id"""
        return Response ({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
