from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, ReadOnlyPasswordHashField
from .models import *
from django.utils.translation import gettext_lazy as _


class CreateNews(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo', 'category']


class ChangeNews(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'photo']
