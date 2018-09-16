from gallery.models import Collection, Work, Photography, Directing, ArtDirecting
from rest_framework import serializers


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('name', 'description', 'id', 'sort_order')


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('name', 'description', 'image', 'dimensions_x',
                  'dimensions_y', 'material', 'collection')


class PhotographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Photography
        fields = ('name', 'image', 'description',
                  'dimensions_x', 'dimensions_y')


class DirectingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directing
        fields = ('name', 'description', 'videoId')


class ArtDirectingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directing
        fields = ('name', 'description', 'videoId')
