from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/profile/<str:pk>', Account.as_view(), name='user_profile'),

    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),

    path('accounts/profile/you/', Account.as_view(), name='account'),
    path('accounts/profile/you/edit', Account.as_view(), name='edit_account'),
]
