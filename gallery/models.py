from django.db import models
import os

def image_upload_handler(self, filename):
    return 'static/images/%s/%s.jpg' % (self.collection.name, self.name)

# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=256,unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Work(models.Model):
    name = models.CharField(max_length=256,unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to=image_upload_handler, default='images/placeholders/no-image.jpg')
    dimensions_x = models.IntegerField()
    dimensions_y = models.IntegerField()
    material = models.CharField(max_length=256)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.collection.name + " : " + self.name


