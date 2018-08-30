from django.contrib import admin

# Register your models here.

from gallery.models import Collection, Work, Photography, ArtDirecting, Directing

admin.site.register(Collection)
admin.site.register(Work)
admin.site.register(Photography)
admin.site.register(Directing)
admin.site.register(ArtDirecting)
