from django.conf.urls import patterns, url
from rcl.views import HistoryView, DCIView, JoinView

urlpatterns = patterns('',
    # Fill with URLs for Rainbow Crystal Lands main page and minipages
    url(r'^history/$', HistoryView.as_view(), name='main-history'),
    url(r'^dci/$', DCIView.as_view(), name='main-dci'),
    url(r'^how-to-join/$', HistoryView.as_view(), name='main-join'),
)
