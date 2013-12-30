# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

from rcl.views import HomePageView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^rcl/', include('rcl.urls', namespace='rcl')),
    url(r'^u/', include('users.urls', namespace='users')),
    
    url(r'^forum/', include('pybb.urls', namespace='pybb')),

    #url(r'^accounts/', include('django.contrib.auth.urls')),
    # django-registration-email urls instead
    url(r'^accounts/', include('registration_email.backends.default.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
