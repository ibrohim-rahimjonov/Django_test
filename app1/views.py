from django.shortcuts import render
from django.http import HttpResponse

from configapp.models import Product


# Create your views here.

def salom1(request):
    return HttpResponse('salom 1 ')

