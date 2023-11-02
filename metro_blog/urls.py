from django.urls import path
from .views import *

urlpatterns = [
    path('', PublicPosts.as_view(), name='blogs'),
    path('post/special/list/', AllPosts.as_view(), name='post_list'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('post/<slug:post_slug>/add_comment/', CommentCreateView.as_view(), name='add_comment'),
    path('post/special/add/', AllPosts.as_view(), name='add_post'),
]
