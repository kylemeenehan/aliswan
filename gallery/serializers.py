from gallery.models import Collection, Work
from rest_framework import serializers

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('name', 'description', 'id')


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('name', 'description', 'image', 'dimensions_x', 'dimensions_y', 'material', 'collection')
