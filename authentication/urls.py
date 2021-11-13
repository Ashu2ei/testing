from django.shortcuts import render
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.urls import path
from authentication.views import RegisterAPIView , LogOutAPIView  ,  Checking
urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterAPIView.as_view()),
    path('api/logout/', LogOutAPIView.as_view(), name = 'logout_view'),
    #path('api/testing/', TestingAPIView.as_view(), name = 'TestingAPIView'),
    path('api/many/', Checking.as_view(), name = 'Checking'),

]