from django.urls import path
from .views import ExternalAPIDataView

urlpatterns = [
    path('registers/', ExternalAPIDataView.as_view(), name='register-list'),
]