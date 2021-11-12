from django.shortcuts import render
from rest_framework.views import APIView
from authentication.models import User
from authentication.serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
import traceback

class TestingAPIView(APIView):
    def get(self, request, format = None):
        try:
            obj = User.objects.get(pk = 3)
            obj.delete()
            return Response({'status':'SUCCESS'},status=200)
        except Exception as e:
            traceback.print_exc()
            return Response({'status':'ERROR','message':str(e)})
