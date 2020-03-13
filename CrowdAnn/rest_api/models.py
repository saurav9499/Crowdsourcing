from django.db import models

# Create your models here.
class Images(models.Model):
    image_id = models.IntegerField()
    image_source = models.URLField()
    is_annotated = models.BooleanField()
    def __str__(self):
        return self.image_source

class Annotated_Images(models.Model):
    image_id = models.IntegerField()
    meta_data = models.CharField(max_length=100)