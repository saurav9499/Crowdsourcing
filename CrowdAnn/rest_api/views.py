from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ImageSerializer
from .models import Images
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
# Create your views here.


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')


class imageList(APIView):
    def get(self, request):
        queryset = Images.objects.all()
        serializer = ImageSerializer(queryset, many = True)
        return Response(serializer.data)



