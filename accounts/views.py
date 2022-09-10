from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from dateutil.relativedelta import relativedelta
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class Login(APIView):

    def post(self, request):
        try:
            user = authenticate(username=request.data.get("email"), password=request.data.get("password"))
            if user:
                access_token = AccessToken.for_user(user)
                refresh_token = RefreshToken.for_user(user)
                data = {
                    'access': str(access_token),
                    'refresh': str(refresh_token)
                }
                return Response({'success': True, 'data': data, 'message': 'user login successfully'},
                                status=status.HTTP_200_OK)
            return Response({'success': False, 'data': None, 'message': 'user does not exist'},
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'success': False, 'data': None, 'message': e.args[0]},
                            status=status.HTTP_400_BAD_REQUEST)

