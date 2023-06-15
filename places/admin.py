from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableTabularInline, SortableAdminBase


class ImageInline(SortableTabularInline):
    model = Image

    fields = (
        'image',
        'get_preview_image',
    )

    readonly_fields = (
        'get_preview_image',
    )

    def get_extra(self, request, obj=None, **kwargs):
        extra = 2
        return extra

    def get_preview_image(self, image):
        return format_html(
            f'<img src="{image.image.url}" width="auto" height="200px"/>'
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'longitude',
        'latitude',
    )
    inlines = [
        ImageInline,
    ]
    search_fields = (
        'title',
    )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = (
        'filename',
    )
