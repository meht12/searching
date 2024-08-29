# api_integration/views.py
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from operator import itemgetter

class ExternalAPIDataView(APIView):
    def get(self, request):
        
        response = requests.get('http://13.127.246.196:8000/api/registers')
        data = response.json()

        
        filter_params = ['name', 'email', 'college_name']
        for param in filter_params:
            param_value = request.query_params.get(param)
            if param_value:
                data = [item for item in data if param_value.lower() in item[param].lower()]

        
        sort_by = request.query_params.get('sort_by')
        if sort_by:
            reverse = sort_by.startswith('-')
            key = sort_by.lstrip('-')
            data = sorted(data, key=itemgetter(key), reverse=reverse)

        return Response(data)
