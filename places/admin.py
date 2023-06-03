from django.contrib import admin
from .models import Place, Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'display_description_short',
        'longitude',
        'latitude',
    )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    # list_display = (
    #     'id',
    #     'place',
    # )
    pass