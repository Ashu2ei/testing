from django.shortcuts import render
from django.urls import path
from student.views import*
urlpatterns = [
    path('api/register/', RegisterAPIView.as_view()),

]