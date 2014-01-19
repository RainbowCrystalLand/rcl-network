# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.contrib.sites.models import RequestSite, Site

from registration.backends.default.views import RegistrationView
from registration import signals
from registration.models import RegistrationProfile


User = get_user_model()

class CustomRegistrationView(RegistrationView):

    def register(self, request, **cleaned_data):
        username, email, password = cleaned_data['username'], cleaned_data['email'], cleaned_data['password1']
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        new_user = RegistrationProfile.objects.create_inactive_user(username, email,
                                                                    password, site)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user
