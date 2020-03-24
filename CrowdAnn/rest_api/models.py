
from django.contrib.gis.db import models
from django.core.validators import int_list_validator
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
# Create your models here.

class Image(models.Model):
    image_id = models.IntegerField(primary_key=True, unique=True)
    image_source = models.URLField()
    provider_id = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.image_source

class Annotation(models.Model):
    annotation_id = models.IntegerField(primary_key=True, unique=True)
    image_id = models.ForeignKey('Image', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    coordinates = ArrayField(models.IntegerField(), null = True)
    label = models.CharField(max_length=300)
    
    def __str__(self):
        return self.label
    



