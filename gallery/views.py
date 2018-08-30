from django.shortcuts import render
from rest_framework import viewsets
from gallery.serializers import CollectionSerializer, WorkSerializer, PhotographySerializer, ArtDirectingSerializer, DirectingSerializer

from gallery.models import Collection, Work, Photography, Directing, ArtDirecting

# Create your views here.


def index(request):
    collections = Collection.objects.all()
    params = {'collections': collections}
    return render(request, 'gallery/index.html', context=params)


def collection(request, collection_name):
    collection = Collection.objects.get(name=collection_name)
    works = Work.objects.filter(collection=collection)
    params = {'collection': collection, 'works': works}
    return render(request, 'gallery/collection.html', params)


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


class PhotographyViewSet(viewsets.ModelViewSet):
    queryset = Photography.objects.all()
    serializer_class = PhotographySerializer


class DirectingViewSet(viewsets.ModelViewSet):
    queryset = Directing.objects.all()
    serializer_class = DirectingSerializer


class ArtDirectingViewSet(viewsets.ModelViewSet):
    queryset = ArtDirecting.objects.all()
    serializer_class = ArtDirectingSerializer
