from django.urls import path
from .views import *

urlpatterns = [
    path('', LastNews.as_view(), name='main'),
]