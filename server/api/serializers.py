from rest_framework import serializers

from users.models import CustomUser
from news.models import CategoryNews, News


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields =['password', 'username', 'first_name', 'last_name', 'email', 'is_active', 'parent',]
        extra_kwargs = {
            'password': {'write_only': True}  # Пароль должен быть только для записи
        }


class CategoryNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryNews
        fields = ['id', 'name']

class NewsSerializer(serializers.ModelSerializer):
    category = CategoryNewsSerializer()  # Вложенный сериализатор для категории
    author = serializers.StringRelatedField()  # Чтобы вывести имя автора вместо его ID
    photo_url = serializers.SerializerMethodField()  # Добавляем метод для генерации полного URL

    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'photo_url', 'time_create', 'time_update', 'category', 'author']

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.photo.url
        return request.build_absolute_uri(photo_url) if request else photo_url