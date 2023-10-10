from django.urls import path
from .views import *

urlpatterns = [
    path('', Cities.as_view(), name='cities_list'),
    path('post/<slug:cities_slug>/', ShowCity.as_view(), name='cities'),
]
