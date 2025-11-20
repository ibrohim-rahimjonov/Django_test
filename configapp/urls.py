from django.urls import path
from configapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/',index)

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
