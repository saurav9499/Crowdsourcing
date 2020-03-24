from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status, viewsets, generics, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.contrib.auth.models import User, Group
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ImageSerializer, UserSerializer, GroupSerializer, AnnotationSerializer
from .models import Image, Annotation
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ImageViewset(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    annotated_images = Annotation.objects.all().values('image_id')
    queryset = Image.objects.exclude(image_id__in=annotated_images)

class AnnotationViewset(viewsets.ModelViewSet):
    serializer_class = AnnotationSerializer
    queryset = Annotation.objects.all()