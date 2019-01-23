from rest_framework import serializers

from gallery.models import ArtDirecting, Collection, Directing, Photography, \
    Work, Contact


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


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    phone = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=100)
    message = serializers.CharField()
    created = serializers.DateTimeField()

    def create(self, validated_data):

        return Contact.objects.create(**validated_data)
