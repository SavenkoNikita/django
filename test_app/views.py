import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Это моё первое приложение')


def time(request):
    return HttpResponse(f'Текущее время - [{datetime.datetime.now().time()}]')
