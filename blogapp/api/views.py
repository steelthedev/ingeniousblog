from django.shortcuts import render
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, response
from .models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@api_view(['GET', 'POST' ])
def BlogView(request):
    try:
        blog = Blog.objects.all()
    except blog.DoesNotExist:
        return HttpResponse(status = 404)
    if request.method == "GET":
        serializer = BlogSerializer(blog , many=True)
        return Response(serializer.data)
    elif request.method == "POST":

        serializer = BlogSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "New blog Created succesfully"
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def ViewPost(request , slug):
    try:
        blog = Blog.objects.get(slug=slug)
    except blog.DoesNotExist:
        return HttpResponse(status = 404 )
    if request.method  == "GET":
        serializer = BlogSerializer(blog , many=True)
        return Response(serializer.data)
    

@api_view(['DELETE', ])
def DeleteBlog(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
    except blog.DoesNotExist:
        return HttpResponse(status = 404 )
    if request.method == "DELETE":
        operation = blog.delete()
        data={}
        if operation:
            data["success"]= "post successfully deleted"
        else:
            data["error"] = "Error deleting post"
        return Response(data=data)

@api_view(['PUT', ])
def UpdateBlog(request , slug):
    try:
        blog = Blog.objects.get(slug=slug)
    except blog.DoesNotExist:
        return HttpResponse(status=404)
    if request.method  == "PUT":
        serializer = BlogSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Update Successful"
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        




