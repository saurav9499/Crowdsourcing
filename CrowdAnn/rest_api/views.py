from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ImageSerializer
from .models import Image
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
# Create your views here.


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')


class getImage(APIView):
    def get(self, request):
        queryset = Image.objects.all()
        serializer = ImageSerializer(queryset, many = True)
        return Response(serializer.data)

class sendData(APIView):
    def put(self, request, coordinates, label):
        if request.method == 'PUT':
            serializer = ImageSerializer(Image, data=request.data, context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



