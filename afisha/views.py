from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, HttpResponse
from places.models import Place


def index(request):
    places = {
        "type": "FeatureCollection",
        "features": [],
    }

    places_data = Place.objects.all()
    for place in places_data:
        places['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": "static/places/roofs24.json"
                }
            }
        )
    return render(request, 'index.html', context={'places': places})


def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_data = {
        "title": place.title,
        "imgs": [img.image.url for img in place.imgs.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude,
        }
    }
    response = JsonResponse(
        place_data,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 2,
        }
    )
    return response
