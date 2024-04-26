from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, ReadOnlyPasswordHashField
from .models import *
from django.utils.translation import gettext_lazy as _


class CreateRecord(ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'age', 'section', 'is_this_a_child']
