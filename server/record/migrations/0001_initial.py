# Generated by Django 5.0.4 on 2024-04-26 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='Имя:')),
                ('last_name', models.CharField(max_length=200, verbose_name='Фамилия:')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('confirmation', models.BooleanField(null=True, verbose_name='Подтверждено')),
                ('is_this_a_child', models.BooleanField(verbose_name='Это ребенок?')),
            ],
        ),
    ]
