from django.db import models
from users.models import CustomUser
from sections.models import Section


class Record(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="Имя:")
    last_name = models.CharField(max_length=200, verbose_name="Фамилия:")
    age = models.IntegerField(verbose_name="Возраст")
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    section = models.ForeignKey(Section, on_delete=models.PROTECT, verbose_name="Секция")
    confirmation = models.BooleanField(verbose_name="Подтверждено", null=True)
    is_this_a_child = models.BooleanField(verbose_name="Это ребенок?")
