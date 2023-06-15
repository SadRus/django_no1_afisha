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
        place_data = response.json()

        place, _ = Place.objects.get_or_create(
            title=place_data['title'],
            description_short=place_data['description_short'],
            description_long=place_data['description_long'],
            longitude=place_data['coordinates']['lng'],
            latitude=place_data['coordinates']['lat'],
        )

        image_urls = place_data['imgs']
        for image_url in image_urls:
            response = requests.get(image_url)
            response.raise_for_status()

            content_file = ContentFile(response.content)
            filename = urlparse(image_url).path.split('/')[-1]
            img = Image.objects.create(place=place)
            img.image.save(filename, content_file, save=True)
