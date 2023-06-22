import requests

from django.core.files.base import ContentFile
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from urllib.parse import urlparse

from places.models import Place, Image


class Command(BaseCommand):
    help = 'download place from JSON by url'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            'url',
            type=str
        )

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        response.raise_for_status()
        raw_place = response.json()

        place, place_is_created = Place.objects.update_or_create(
            title=raw_place['title'],
            defaults={
                'description_short': raw_place.get('description_short', ''),
                'description_long': raw_place.get('description_long', ''),
                'longitude': raw_place['coordinates']['lng'],
                'latitude': raw_place['coordinates']['lat'],
            }
        )
        if place_is_created:
            image_urls = raw_place.get('imgs', [])
            for image_url in image_urls:
                response = requests.get(image_url)
                response.raise_for_status()

                filename = urlparse(image_url).path.split('/')[-1]
                content_file = ContentFile(response.content, name=filename)
                Image.objects.create(
                    place=place,
                    image=content_file,
                )
