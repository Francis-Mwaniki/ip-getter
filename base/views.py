from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.http import HttpResponse
from rest_framework.decorators import api_view
import socket
from ip2geotools.databases.noncommercial import DbIpCity

@api_view(['GET'])
def home(request):
    # user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    # if user_ip:
    #     ip = user_ip.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')
    
    #return HttpResponse("Welcome User!<br>You are visiting from: {}".format(ip))
    pass
