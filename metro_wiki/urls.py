from django.urls import path
from .views import *

urlpatterns = [
    path('city/<slug:cities_slug>/', ShowCity.as_view(), name='cities'),
    path('line/<slug:line_slug>/', ShowLine.as_view(), name='line'),
    path('station/<slug:station_slug>/', ShowStation.as_view(), name='station'),
]
