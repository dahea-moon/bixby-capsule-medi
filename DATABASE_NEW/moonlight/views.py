from django.shortcuts import render, HttpResponse
from .models import Moonlight
from bound import Bound
import json

days = {'monday': 'day1', 'tuesday': 'day2', 'wendesday': 'day3', 'thursday': 'day4', 'friday': 'day5', 'saturday': 'day6', 'sunday': 'day7'}

def search_nearest(request):
    user_data = json.loads(request.GET)
    current_location = (langt, longt)
    # current_day = days[day]

    LC = Bound(langt, longt)
    result = Moonlight.objects.filter(
        Q(langt__range=[LC['langt_min'], LC['langt_max']]) &
        Q(longt__range=[LC['longt_min'], LC['longt_max']])
    )
    return HttpResponse(result)
