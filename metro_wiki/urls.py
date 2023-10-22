from django.urls import path
from .views import *

urlpatterns = [
    path('post/<slug:cities_slug>/', ShowCity.as_view(), name='cities'),
    path('post/<slug:line_slug>/', ShowLine.as_view(), name='line'),
]
