from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(dir(request))
    return HttpResponse(print(request))