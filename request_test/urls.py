from django.urls import path
from .views import get_request_info

urlpatterns = [
    path('request-info/', get_request_info, name='request_info')
]