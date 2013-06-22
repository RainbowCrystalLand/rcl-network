from django.http import HttpResponse
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'rcl/main/home.html'


class HistoryView(TemplateView):
    template_name = 'rcl/main/history.html'


class DCIView(TemplateView):
    template_name = 'rcl/main/dci.html'


class JoinView(TemplateView):
    template_name = 'rcl/main/join.html'