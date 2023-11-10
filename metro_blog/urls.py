from django.urls import path
from .views import *

urlpatterns = [
    path('', PublicPosts.as_view(), name='blogs'),
    path('post/special/list/', AllPosts.as_view(), name='post_list'),
    path('post/special/user_list/', UserPosts.as_view(), name='post_user_list'),

    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('post/<slug:post_slug>/comment', AddComment.as_view(), name='post_comment'),

    path('post/special/add/', AddPost.as_view(), name='add_post'),
    path('post/<slug:post_slug>/update/', UpdatePost.as_view(), name='update_post'),
    path('post/<slug:post_slug>/delete/', PostDelete.as_view(), name='delete_post'),
]
