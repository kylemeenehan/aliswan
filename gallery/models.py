from django.db import models

# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name

class Work(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/placeholders/no-image.jpg')
    dimensions_x = models.IntegerField()
    dimensions_y = models.IntegerField()
    material = models.CharField(max_length=256)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.collection.name + " : " + self.name
