from django.db import models
import os


def image_upload_handler(self, filename):
    return 'static/images/%s/%s.jpg' % (self.collection.name, self.name)


def photo_upload_handler(self, filename):
    return 'static/photos/%s.jpg' % (self.name)
# Create your models here.


class Collection(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    sort_order = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Work(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    image = models.ImageField(
        upload_to=image_upload_handler,
        default='placeholders/no-image.jpg')
    dimensions_x = models.IntegerField()
    dimensions_y = models.IntegerField()
    material = models.CharField(max_length=256)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.collection.name + " : " + self.name


class Directing(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    videoId = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ArtDirecting(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    videoId = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Photography(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    image = models.ImageField(
        upload_to=photo_upload_handler,
        default='placeholders/no-image.jpg')
    dimensions_x = models.IntegerField()
    dimensions_y = models.IntegerField()

    def __str__(self):
        return self.name
