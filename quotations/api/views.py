from rest_framework.views import APIView
from rest_framework.response import Response


class QuotationsView(APIView):
    def get(self, request, format=None):
        """
        Post an article like.
        """
        return Response("Test response")
