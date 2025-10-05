from django.contrib import admin
from .models import AuthorInfo, Collection, ArtGroup, Artwork, Appeal

# Register your models here.
admin.site.register(AuthorInfo)
admin.site.register(Collection)
admin.site.register(ArtGroup)
admin.site.register(Artwork)
admin.site.register(Appeal)