from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from . serializer import UserLoginSerializer




class UserLoginView(TokenObtainPairView):
    """
        This API is used to login the user. \n
        The username and password must be passed in the request body.
    """
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        
        refresh = RefreshToken.for_user(serializer.validated_data['user'])
        return Response(
                {"access": str(refresh.access_token)}, 
                status=status.HTTP_200_OK
            )