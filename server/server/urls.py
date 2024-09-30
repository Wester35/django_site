from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


def index(request):
    return HttpResponse("Hello")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sections/', include('sections.urls')),
    path('record/', include('record.urls')),
    path('user/', include('users.urls')),
    path('news/', include('news.urls')),
    path('api/', include('api.urls')),
    path('', include('main.urls')),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
