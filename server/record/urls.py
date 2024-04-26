from django.urls import path
from .views import *


urlpatterns = [
    path('', RecordlineList.as_view(), name='record'),
    path('create/', RecordCreate.as_view(), name='create_record'),
    path('update/<int:pk>/', RecordUpdate.as_view(), name='update_record'),
    path('<int:pk>/', RecordDetail.as_view(), name='record_datail'),
]
