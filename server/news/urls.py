from django.urls import path
from .views import *


urlpatterns = [
    path('', NewslineList.as_view(), name='news'),
    path('create/', NewslineCreate.as_view(), name='create_news'),
    path('update/<int:pk>/', NewsUpdate.as_view(), name='update_news'),
    path('<int:pk>/', NewsDetail.as_view(), name='news_datail'),
]
