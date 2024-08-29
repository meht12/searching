# api_integration/views.py
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from operator import itemgetter

class ExternalAPIDataView(APIView):
    def post(self, request):
        # Fetch data from the external API
        try:
            response = requests.get('http://13.127.246.196:8000/api/registers')
            response.raise_for_status()  # Raise an exception for bad status codes
            data = response.json()
        except requests.RequestException as e:
            return Response({"error": f"Failed to fetch data from external API: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Extract filtering and sorting options from request body
        filters = request.data.get('filters', {})
        sort_by = request.data.get('sort_by')

        # Manual filtering based on provided options
        for param, param_value in filters.items():
            if param_value:
                data = [item for item in data if param_value.lower() in item.get(param, '').lower()]

        # Apply sorting
        if sort_by:
            reverse = sort_by.startswith('-')
            key = sort_by.lstrip('-')
            try:
                data = sorted(data, key=itemgetter(key), reverse=reverse)
            except KeyError:
                return Response({"error": f"Invalid sorting key: {key}"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data)