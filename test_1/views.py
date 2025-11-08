from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def get_json(request):
    data = {
        1:{
        "name": "Ibrohim",
        "surname": "R ",
        "age": "25",
        "phone": "+998901231212",
    },
    2:{ "name": "Ali",
        "surname": "R ",
        "age": "25",
        "phone": "+998901231212",

        }}
    return JsonResponse(data)