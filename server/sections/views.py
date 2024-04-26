from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView
from .models import *
from .forms import *
from django.shortcuts import redirect

class SectionsCreate(LoginRequiredMixin, CreateView):
    template_name = "sections/sections_index.html"
    form_class = CreateSectionsForm

    def get_success_url(self):
        return reverse_lazy('main')

    def get(self, request, *args, **kwargs):
        if (self.request.user.rights == 2 or self.request.user.rights == 0):
            return super().get(request, *args, **kwargs)

        return redirect('main')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить публикацию'
        context['name_title_form'] = 'Добавить публикацию'
        context['name_button'] = 'Добавить'
        return context

class SectionslineList(ListView):
    template_name = "sections/sections_news_line.html"
    model = Section
    context_object_name = 'posts'

    extra_context = {'title': 'Секции'}

class SectionsDetail(DetailView):
    template_name = "sections/sections_detail.html"
    model = Section
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Публикация'
        context['name_title_form'] = ''
        return context

class SectionsUpdate(LoginRequiredMixin, UpdateView):
    template_name = "sections/sections_index.html"
    model = Section

    fields = ['name', 'content', 'photo']

    def get_success_url(self):
        return reverse_lazy('main')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if (self.request.user == self.object.author):
            return super().get(request, *args, **kwargs)

        return redirect('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование секции'
        context['name_title_form'] = 'Редактировать секцию'
        context['name_button'] = 'Редактировать'
        return context