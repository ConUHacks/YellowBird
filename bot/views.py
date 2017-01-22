from django.shortcuts import render
from django.http import HttpResponse
from .models import Query

from bot.static.bot.py import yellowpages

def query(request):
    return render(request, 'bot/query.html')

def result(request):
    concept = request.POST['concept'];
    location_x = request.POST['location_x'];
    location_y = request.POST['location_y'];
    Query.objects.create(concept=concept, location_x=location_x, location_y=location_y)

    location = location_x + "," + location_y
    yellowpages.query_yp(concept,location)

    return render(request, 'bot/result.html')