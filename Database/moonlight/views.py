import json
from haversine import haversine
from .models import Moonlight

def search_nearest(request, longt, langt, time):
    longt = float(longt)
    langt = float(langt)
    current_location = (langt, longt)
    

    return json.dump()


def searchbyplace(request):
    return


def searchbytime(request):
    return


def searchbyday(request):
    return