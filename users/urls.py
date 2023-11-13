from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('profile/<str:profile_pk>/', Account.as_view(), name='user_profile'),
    path('profile/<str:profile_pk>/edit', EditUser.as_view(), name='user_profile_edit'),

    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),

    path('account/', UserAccount.as_view(), name='user'),
]
