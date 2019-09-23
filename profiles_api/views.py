from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns features"""
        an_apiview = [
            'User HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to urls',
        ]

        return Response ({'message': 'Hello !', 'An API View is here': an_apiview})
