from django.shortcuts import render
from rest_framework.views import APIView
from authentication.models import User
from authentication.serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
import traceback

class RegisterAPIView(APIView):
    serializer_class = UserRegisterSerializer
    def post(self, request, *args, **kwargs):    
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid(raise_exception = True):
                user = serializer.save()
                refresh = RefreshToken.for_user(user)
                response_data = {
                    'refresh' : str(refresh),
                    'access'  : str(refresh.access_token),
                    'user'    : serializer.data,
                }
            return Response({'status':'SUCCESS','data':response_data},status=200)
        except Exception as e:
            traceback.print_exc()
            return Response({'status':'ERROR','message':str(e)})


class LogOutAPIView(APIView):
    def post(self, request, format = None):
        # token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]#SPLIT THE TOKEN WITH SPACE AND PICK UP THE TOKEN FROM 1ST INDEX
        # print(token)
        # return Response({'status':'SUCCESS'},status=200)
        try:
            refresh_token = request.data.get('refresh_token')
            token_obj = RefreshToken(refresh_token)
            token_obj.blacklist()
            return Response({'status':'Log Outr Successfully'},status = status.HTTP_200_OK)
        except Exception as e:
            return Response(status = status.HTTP_400_OK)


########################################CHANGE PASSWORD

class TestingAPIView(APIView):
    def get(self, request, format = None):
        try:
            obj = User.objects.get(pk = 3)
            obj.delete()
            return Response({'status':'SUCCESS'},status=200)
        except Exception as e:
            traceback.print_exc()
            return Response({'status':'ERROR','message':str(e)})

