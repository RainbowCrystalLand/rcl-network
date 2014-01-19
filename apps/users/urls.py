# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from users.views import UserUpdateView, DashboardView
from django.contrib.auth.decorators import login_required

from settings import LOGIN_URL


urlpatterns = patterns('',
    url(r'^dashboard/$', login_required(login_url=LOGIN_URL)(DashboardView.as_view()), name='dashboard'),
    url(r'^profile/edit/$', login_required(login_url=LOGIN_URL)(UserUpdateView.as_view()), name='profile-edit'),
)
