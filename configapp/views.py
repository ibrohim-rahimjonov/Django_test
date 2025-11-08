from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def salom(request):
    return HttpResponse("Salom")

def dunyo(request):
    return HttpResponse("dars1 uchun mahsus ")