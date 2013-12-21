from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'rcl/main/home.html'


class HistoryView(TemplateView):
    template_name = 'rcl/main/history.html'


class DCIView(TemplateView):
    template_name = 'rcl/main/dci.html'


class JoinView(TemplateView):
    template_name = 'rcl/main/join.html'


class WelcomeView(TemplateView):
    template_name = 'rcl/main/welcome.html'


class RegistrationSuccessfulView(TemplateView):
    template_name = 'rcl/main/registration_successful.html'
