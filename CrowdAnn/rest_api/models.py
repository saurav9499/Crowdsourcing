
from django.contrib.gis.db import models

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
    user = models.IntegerField()
    coordinates = models.PolygonField(null=True)
    label = models.CharField(max_length=300)
    
    def __str__(self):
        return self.label
    



