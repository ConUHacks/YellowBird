from django.shortcuts import render
from django.http import HttpResponse

def query(request):
    return render(request, 'bot/query.html')

def result(request):
    return render(request, 'bot/result.html')