from django.urls import path
from .views import *
from main_page import views

urlpatterns = [
    path('', LastNews.as_view(), name='main'),
    path('', views.cities, name='main_cities'),
]
