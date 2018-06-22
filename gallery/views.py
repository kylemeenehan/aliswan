from django.shortcuts import render

from gallery.models import Collection, Work

# Create your views here.

def index(request):
    collections = Collection.objects.all()
    params = { 'collections': collections }
    return render(request, 'gallery/index.html', context=params)

def collection(request, collection_name):
    collection = Collection.objects.get(name=collection_name)
    works = Work.objects.filter(collection=collection)
    params = { 'collection': collection, 'works': works }
    return render(request, 'gallery/collection.html', params)


