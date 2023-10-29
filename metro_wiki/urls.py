from django.urls import path
from .views import *

urlpatterns = [
    path('city/', Cities.as_view(), name='cities'),
    path('line/', Lines.as_view(), name='lines'),
    path('station/', Stations.as_view(), name='stations'),

    path('city/<slug:city_slug>/', ShowCity.as_view(), name='city'),
    path('line/<slug:line_slug>/', ShowLine.as_view(), name='line'),
    path('station/<slug:station_slug>/', ShowStation.as_view(), name='station'),

    path('station/add/station', AddStation.as_view(), name='add_station'),
]
