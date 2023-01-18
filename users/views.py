from django.shortcuts import render,redirect

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import useSerializer,UserSerializer
from .models import CustomUser
from django.contrib.auth import get_user_model, logout,get_user
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import AuthenticationFailed


def mainUser(request):
    user = get_user(request.user)
    print(f'{get_user(request.user)}')
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)
 

class register(APIView):
    def post(self,request):
        data=request.data
        serializer = useSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class Login(APIView):
    def post(self,request):
        user = get_user_model().is_authenticated
        if request.user==user:
             return redirect('home')

        email=request.data['email']
        password=request.data['password'] 
        
        user=CustomUser.objects.filter(email=email).first()
        
        
        if user is None:
            raise AuthenticationFailed('User is not found')
        if user.password != password:
            raise AuthenticationFailed('Incorrect Password')
        
        return Response({'details':"Logged in"})

def custom_Logout(request):
    logout(request=request)
    return redirect('home')