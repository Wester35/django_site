from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, ReadOnlyPasswordHashField
from django.forms import ModelForm

from .models import *
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    USERNAME_FIELD = 'email'

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'parent')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'password', 'email', 'parent')


class CustomAuthenticationForm(AuthenticationForm):
    password = forms.CharField(
        label=_("Пароль:"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    username = forms.CharField(label=_("Номер телефона, почта или логин:"), widget=forms.TextInput(attrs={"autofocus": True, "class": "login"}))
