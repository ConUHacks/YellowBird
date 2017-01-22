from django.shortcuts import render
from django.http import HttpResponse

from bot.static.bot.py import yellowpages

def query(request):
    return render(request, 'bot/query.html')

def result(request):

    concept = "food";
    location = "45.4754418,-73.5863705";

    yellowpages.query_yp(concept,location)

    return render(request, 'bot/result.html')