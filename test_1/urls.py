from django.urls import path
from test_1.views import *

urlpatterns = [
    path('json/',get_json)

]