"""aliswan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from gallery import views

router = routers.DefaultRouter()
router.register(r'collections', views.CollectionViewSet)
router.register(r'works', views.WorkViewSet)
router.register(r'photography', views.PhotographyViewSet)
router.register(r'artdirecting', views.ArtDirectingViewSet)
router.register(r'directing', views.DirectingViewSet)
# router.register(r'contact', views.ContactViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('gallery/', views.index),
    path('gallery/collection/<str:collection_name>', views.collection),
    path('admin/', admin.site.urls),
]
