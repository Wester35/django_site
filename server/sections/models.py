from django.db import models
from users.models import CustomUser


class Section(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название:")
    content = models.TextField(verbose_name="О секции:")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото:")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания:")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата последнего редактирования:")
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
