from django.urls import path
from .views import *

urlpatterns = [
    path('', SectionslineList.as_view(), name='sections_list'),
    path('create/', SectionsCreate.as_view(), name='sections_create'),
    path('update/<int:pk>/', SectionsUpdate.as_view(), name='sections_update'),
    path('<int:pk>/', SectionsDetail.as_view(), name='section'),
]