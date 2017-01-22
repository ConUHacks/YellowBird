from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Query

import json
from .static.bot.py import nuance
from .static.bot.py import yellowpages

def index(request):
    return render(request, 'bot/index.html')

def bootstrap(request):
    return render(request, 'bot/bootstrap.min.css')

def query(request):
    return render(request, 'bot/query.html')

def result(request):
    try:
        chat = request.POST['chat'];
        print("captured from query input:" + chat)
    except ValueError:
        print("Error: nuance query returned invalid value")
        chat = "food"

    # # nuance api call when it works
    # try:
    #     query_nuance_result = nuance.query_nuance(chat)
    # except ValueError:
    #     return Http404()

    # yellowpages api call
    try:
        query_yellowpages_result = yellowpages.query_yp(chat)
    except ValueError:
        return Http404()

    coords_0 = [float(query_yellowpages_result[0]['centroid'].split(",")[0]), float(query_yellowpages_result[0]['centroid'].split(",")[1])]
    coords_1 = [float(query_yellowpages_result[1]['centroid'].split(",")[0]), float(query_yellowpages_result[1]['centroid'].split(",")[1])]
    coords_2 = [float(query_yellowpages_result[2]['centroid'].split(",")[0]), float(query_yellowpages_result[2]['centroid'].split(",")[1])]
    coords_3 = [float(query_yellowpages_result[3]['centroid'].split(",")[0]), float(query_yellowpages_result[3]['centroid'].split(",")[1])]

    context = {
        'results_head_0' : { 'name': query_yellowpages_result[0]['businessName'] , 'coords': coords_0},
        'results_head_1': {'name': query_yellowpages_result[1]['businessName'], 'coords': coords_1},
        'results_head_2': {'name': query_yellowpages_result[2]['businessName'], 'coords': coords_2},
        'results_head_3': {'name': query_yellowpages_result[3]['businessName'], 'coords': coords_3},
    }
    return render(request, 'bot/result.html', context)