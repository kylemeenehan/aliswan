from django.contrib import admin

# Register your models here.

from gallery.models import Collection, Work

admin.site.register(Collection)
admin.site.register(Work)
