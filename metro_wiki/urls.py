from django.urls import path
from .views import *

urlpatterns = [
    path('city/', Cities.as_view(), name='cities'),
    path('line/', Lines.as_view(), name='lines'),
    path('station/', Stations.as_view(), name='stations'),
    path('train/', Trains.as_view(), name='trains'),
    path('depot/', Depots.as_view(), name='depots'),

    path('city/<slug:city_slug>/', ShowCity.as_view(), name='city'),
    path('line/<slug:line_slug>/', ShowLine.as_view(), name='line'),
    path('station/<slug:station_slug>/', ShowStation.as_view(), name='station'),
    path('train/<slug:train_slug>/', ShowTrain.as_view(), name='train'),
    path('depot/<slug:depot_slug>/', ShowDepot.as_view(), name='depot'),

    path('city/special/add/', AddCity.as_view(), name='add_city'),
    path('line/special/add/', AddLine.as_view(), name='add_line'),
    path('station/special/add/', AddStation.as_view(), name='add_station'),
    path('train/special/add/', AddTrain.as_view(), name='add_train'),
    path('depot/special/add/', AddDepot.as_view(), name='add_depot'),

    path('station/special/search/', StationSelectorResult.as_view(), name='search_station'),

    path('city/<slug:city_slug>/update/', UpdateCity.as_view(), name='update_city'),
    path('line/<slug:line_slug>/update/', UpdateLine.as_view(), name='update_line'),
    path('station/<slug:station_slug>/update/', UpdateStation.as_view(), name='update_station'),
    path('train/<slug:train_slug>/update/', UpdateTrain.as_view(), name='update_train'),
    path('depot/<slug:depot_slug>/update/', UpdateDepot.as_view(), name='update_depot'),

    path('city/<slug:city_slug>/delete/', DeleteCity.as_view(), name='delete_city'),
    path('line/<slug:line_slug>/delete/', DeleteLine.as_view(), name='delete_line'),
    path('station/<slug:station_slug>/delete/', DeleteStation.as_view(), name='delete_station'),
    path('train/<slug:train_slug>/delete/', DeleteTrain.as_view(), name='delete_train'),
    path('depot/<slug:depot_slug>/delete/', DeleteDepot.as_view(), name='delete_depot'),
]
