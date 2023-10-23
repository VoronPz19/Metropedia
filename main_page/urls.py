from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', LastNews.as_view(), name='main'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='main_page/logout.html'), name='logout'),
    path('accounts/profile/', Account.as_view(), name='account'),
]
