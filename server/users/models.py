from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    rights = models.IntegerField(verbose_name='rights', error_messages="Enter your phone number", null=True)
    parent = models.ForeignKey('CustomUser', on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})