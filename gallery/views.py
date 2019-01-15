from django.shortcuts import render
from rest_framework import request, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from gallery.models import ArtDirecting, Collection, Directing, Photography, \
    Work, Contact
from gallery.serializers import ArtDirectingSerializer, CollectionSerializer, \
    ContactSerializer, DirectingSerializer, PhotographySerializer, \
    WorkSerializer


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


# class ContactViewSet(request):
#     queryset = ArtDirecting.objects.all()
#     serializer = ContactSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
    # return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
