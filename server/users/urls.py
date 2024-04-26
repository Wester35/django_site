from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django_email_verification import urls as email_urls
from .views import *


# Create your views here.
def geeks_view(request):
    return render(request, "users/notion_email.html")

def index(request):
    logout(request)
    return redirect('main')


urlpatterns = [
    path('email/', include(email_urls), name='email-verification'),
    path('logout/', index, name='logout'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('<int:pk>/', DetailUser.as_view(), name='user_detail'),
    path('update/<int:pk>/', UpdateUser.as_view(), name='user_update'),
    path('email/notion/', geeks_view, name='email-notion'),
]
