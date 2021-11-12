from django.urls import path
from testing.views import TestingAPIView



urlspatterns = [
    path('api/testing/', TestingAPIView.as_view(), name='TestingAPIView'),
]