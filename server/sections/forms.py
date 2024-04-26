from django.forms import ModelForm
from .models import *
class CreateSectionsForm(ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'content', 'photo']