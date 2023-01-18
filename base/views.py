from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
import socket
 

@api_view(['GET'])
def home(request):
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        ip = user_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    return Response(format(ip))
