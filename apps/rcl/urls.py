from django.conf.urls import patterns, url
from rcl.views import (HistoryView, DCIView, JoinView, WelcomeView, 
	RegistrationSuccessfulView)

urlpatterns = patterns('',
    # Fill with URLs for Rainbow Crystal Lands main page and minipages
    url(r'^history/$', HistoryView.as_view(), name='main-history'),
    url(r'^dci/$', DCIView.as_view(), name='main-dci'),
    url(r'^how-to-join/$', JoinView.as_view(), name='main-join'),
    url(r'^welcome/$', WelcomeView.as_view(), name='main-welcome'),
    url(r'^activate/$', RegistrationSuccessfulView.as_view(), 
    	name='main-registration-successful'),
)
