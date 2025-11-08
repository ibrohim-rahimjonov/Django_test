from django.urls import path
from configapp.views import *

urlpatterns = [

    path('salom/',salom),
    path('dunyo/',dunyo),

]