from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import *
from .forms import *


class RecordCreate(LoginRequiredMixin, CreateView):
    template_name = "record/index.html"
    form_class = CreateRecord

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.confirmation = 0
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('record')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Записаться на секцию'
        context['name_button'] = 'Записаться'
        return context


class RecordUpdate(LoginRequiredMixin, UpdateView):
    template_name = "record/index.html"
    model = Record

    fields = ['first_name', 'last_name', 'age', 'section']

    def get_success_url(self):
        return reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if (self.request.user == self.object.user):
            return super().get(request, *args, **kwargs)

        return redirect('news')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование записи'
        context['name_title_form'] = 'Редактировать'
        context['name_button'] = 'Редактировать'
        return context


class RecordDetail(LoginRequiredMixin, DetailView):
    template_name = "record/detail.html"
    model = Record
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Секция'
        context['name_title_form'] = 'Ваша секция!'
        return context


class RecordlineList(LoginRequiredMixin, ListView):
    template_name = "record/news_line.html"
    model = Record
    context_object_name = 'posts'

    def get_queryset(self):
        return Record.objects.all().filter(user=self.request.user)

    extra_context = {'title': 'Статьи'}
