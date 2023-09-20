from django.urls import path
from .views import *

urlpatterns = [
    path('', Blogs.as_view(), name='blogs'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
]
