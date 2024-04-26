from django.db import models
from django.urls import reverse
from users.models import CustomUser


class CategoryNews(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name="Заголовок:")
    content = models.TextField(verbose_name="Контент:")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото:")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания:")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата последнего редактирования:")
    category = models.ForeignKey('CategoryNews', on_delete=models.PROTECT, verbose_name="Категория статьи:")
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('news_datail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


