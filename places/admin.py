from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class ImageInline(admin.TabularInline):
    model = Image

    fields = (
        'image',
        'get_preview_image',
        'position',
    )

    try:
        readonly_fields = (
            'get_preview_image',
        )
    except Exception as err:
        print(Exception, err)

    def get_preview_image(self, obj):
        url = obj.image.url
        return format_html(
            "<b>{}</b>",
            mark_safe(f'<img src="{url}" width="auto" height="150px"/>'),
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'display_description_short',
        'longitude',
        'latitude',
    )
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
