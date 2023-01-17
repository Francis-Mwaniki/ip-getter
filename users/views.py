from django.shortcuts import render

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import useSerializer
from .models import CustomUser
from rest_framework.exceptions import AuthenticationFailed


class register(APIView):
    def post(self,request):
        data=request.data
        serializer = useSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class Login(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password'] 
        
        user=CustomUser.objects.filter(email=email).first()
        
        
        if user is None:
            raise AuthenticationFailed('User is not found')
        if user.password != password:
            raise AuthenticationFailed('Incorrect Password')
        
        return Response({'message':"Logged in"})
           