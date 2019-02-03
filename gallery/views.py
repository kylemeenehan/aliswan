from django.shortcuts import render
from rest_framework import request, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.views.decorators.csrf import csrf_exempt

from gallery.models import ArtDirecting, Collection, Contact, Directing, \
    Photography, Work
from gallery.serializers import ArtDirectingSerializer, CollectionSerializer, \
    ContactSerializer, DirectingSerializer, PhotographySerializer, \
    WorkSerializer


import smtplib
from email.message import EmailMessage

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
#     serializer = ContactSerializer(data=request.DATA)
#     if serializer.is_valid():
#         serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # else:
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ContactViewSet(request):
@csrf_exempt
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def contact(request):
        # data = JSONParser().parse(request)

    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # try:

        message = """\
Subject: Aliswan! New Contact Message received!

"Hi Aliswan! Someone has added a new contact! Details below:

Name: %s
Phone: %s
Email: %s
Message: %s
""" % (request.data['name'], request.data['phone'], request.data['email'], request.data['message'])

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
            s.ehlo()
            s.login('mchrisyd@gmail.com', 'Ic3cr3am!2!#YD')
            s.sendmail('mchrisyd@gmail.com', 'haai@aliswan.co.za', message)
            s.close()
        # except (ex):
        #     print(ex)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
