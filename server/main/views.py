from django.conf import settings
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_button'] = 'Дарова'
        context['MEDIA_URL'] = settings.MEDIA_URL  # Добавляем MEDIA_URL в контекст
        return context
