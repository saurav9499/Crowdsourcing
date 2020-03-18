from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Image, Annotation

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['image_source']
     
class AnnotationSerializer(serializers.HyperlinkedModelSerializer):
        model = Annotation
        fields = ['image_id', 'coordinates', 'label']