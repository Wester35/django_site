from django.urls import path
from .views import HomePageView
from django.conf.urls.static import static
from server import settings

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)