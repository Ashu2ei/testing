from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
import traceback



class   RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):    
        try:
            print('hieee')
            return Response({'status':'SUCCESS','data':"response_data"},status=200)
        except Exception as e:
            traceback.print_exc()
            return Response({'status':'ERROR','message':str(e)})