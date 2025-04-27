from django.urls import path
from .views import Example


urlpatterns = [
    path('', Example.as_view(), name='hello')
]