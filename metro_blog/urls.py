from django.urls import path
from .views import *

urlpatterns = [
    path('', Blogs.as_view(), name='blogs'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('add_post/', AddPost.as_view(), name='add_post'),
]
