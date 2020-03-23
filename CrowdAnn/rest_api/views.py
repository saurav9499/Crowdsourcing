from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ImageSerializer, AnnotationSerializer
from .models import Image, Annotation
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
# Create your views here.


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')

class getImage(APIView):
    def get(self, request):
        annotated_images = Annotation.objects.all().values('image_id')
        queryset = Image.objects.exclude(image_id__in=annotated_images)
        serializer = ImageSerializer(queryset, many = True)
        return Response(serializer.data)


class sendData(APIView):
    def put(self, request, coordinates, label):
        if request.method == 'PUT':
            serializer = AnnotationSerializer(coordinates, data=request.data, context={'request':request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



