from contextlib import nullcontext

from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from users.models import CustomUser
from .serializers import UserProfileSerializer
from django_email_verification import send_email  # Импорт функции отправки email

@api_view(['POST'])
def create_user_profile(request):
    try:
        if request.method == 'POST':
            serializer = UserProfileSerializer(data=request.data)
            if serializer.is_valid():
                # Извлекаем данные из сериализатора
                username = serializer.validated_data.get('username')
                password = serializer.validated_data.get('password')

                # Проверяем, существует ли уже пользователь с таким именем
                if CustomUser.objects.filter(username=username).exists():
                    return Response({"detail": "Пользователь с таким именем уже существует."}, status=status.HTTP_400_BAD_REQUEST)

                # Создаем нового пользователя
                user = CustomUser(
                    username=username,
                    password=password,
                    first_name=serializer.validated_data.get('first_name', "Иваг"),
                    last_name=serializer.validated_data.get('last_name', "Гави"),
                    email=serializer.validated_data.get('email'),
                    is_active=serializer.validated_data.get('is_active', False),  # Если у вас есть это поле
                    parent=serializer.validated_data.get('parent', None)
                )
                user.set_password(password)  # Хэширование пароля
                user.save()

                # Отправляем письмо для подтверждения email
                send_email(user)  # Здесь отправляется email с подтверждением

                return Response({"detail": "Пользователь успешно создан. Проверьте вашу почту для подтверждения."}, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        print(f"\n\nERROR: {e}\n\n")
        return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# views.py
@api_view(['POST'])
def check_user(request):
    if request.method == 'POST':
        # Здесь мы создаем отдельный сериализатор только для проверки
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"detail": "Необходимо указать имя пользователя и пароль."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):
                return Response({"detail": "Пользователь успешно аутентифицирован."}, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Неверный пароль."}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({"detail": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)

    return Response({"detail": "Неправильный метод запроса."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
