from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from places.models import Place


def index(request):
    features = []
    for place in Place.objects.all():
        features.append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.longitude, place.latitude]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': reverse('places', args=[place.id])
                }
            }
        )
    places = {
        'type': 'FeatureCollection',
        'features': features,
    }
    return render(request, 'index.html', context={'places': places})


def get_place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    serialize_place = {
        'title': place.title,
        'imgs': [image.image.url for image in place.imgs.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude,
        }
    }
    json_dumps_params = {
        'ensure_ascii': False,
        'indent': 2,
    }
    return JsonResponse(serialize_place, json_dumps_params=json_dumps_params)
