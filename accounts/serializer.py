from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework import exceptions




class UserLoginSerializer(serializers.Serializer):
    
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
    
    def validate(self,attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        user = authenticate(username=username,password=password)
        
        if not user:
            raise exceptions.AuthenticationFailed(detail='Invalid Credentials')
        
        attrs['user']=user
        return attrs
    