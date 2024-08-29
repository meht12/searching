# api_integration/filters.py
import django_filters
from django_filters import rest_framework as filters

class ExternalAPIDataFilter(filters.FilterSet):
    search = django_filters.CharFilter(method='filter_by_search')
    sort_by = django_filters.OrderingFilter(fields=['name', 'email', 'date_registered'])

    class Meta:
        model = None  # Since we're working with an external API, we won't use a model

    def filter_by_search(self, queryset, name, value):
        return [item for item in queryset if value.lower() in item['name'].lower() or value.lower() in item['email'].lower()]
