import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Это моё первое приложение')


def time(request):
    time_now = datetime.datetime.now().time()
    return HttpResponse(f'Текущее время - [{time_now}]')
