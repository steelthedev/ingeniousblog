from django.shortcuts import render
from api.serializers import *
from .models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, response
from django.core.exceptions import ObjectDoesNotExist



@api_view(['POST', ])
def RegisterUser(request):
    if request.method =="POST":
        serializer = RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            user = serializer.save()
            data["response"]="successfully registered a new user"
            data["email"]=user.email
            data["username"]=user.username
        else:
            data=serializer.errors
        return Response(data)
