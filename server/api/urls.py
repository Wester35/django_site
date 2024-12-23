from django.urls import path, include
from .views import create_user_profile, check_user, NewsListAPIView

urlpatterns = [
    path('create-user/', create_user_profile, name='create_user_profile'),
    path('check_user/', check_user, name='check_user'),
    path('news/', NewsListAPIView.as_view(), name='news-list'),
]
