from rest_framework import serializers

from users.models import CustomUser


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields =['password', 'username', 'first_name', 'last_name', 'email', 'is_active', 'parent',]
        extra_kwargs = {
            'password': {'write_only': True}  # Пароль должен быть только для записи
        }