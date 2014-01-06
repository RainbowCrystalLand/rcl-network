# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url


from rcl.views import HomePageView
from pybb_custom.views import CustomAddPostView
from custom_registration.forms import CustomEmailRegistrationForm
from custom_registration.backends import CustomRegistrationView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^rcl/', include('rcl.urls', namespace='rcl')),
    url(r'^u/', include('users.urls', namespace='users')),
    
    # Overrides to fix an error when using the User's email to login
    url('^forum/forum/(?P<forum_id>\d+)/topic/add/$', CustomAddPostView.as_view(), name='add_topic'),
    url('^fortum/topic/(?P<topic_id>\d+)/post/add/$', CustomAddPostView.as_view(), name='add_post'),
    url(r'^forum/', include('pybb.urls', namespace='pybb')),

    #url(r'^accounts/', include('django.contrib.auth.urls')),
    # django-registration-email urls instead
    # Override url to use custom form
    url(
        r'^accounts/register/$',
        CustomRegistrationView.as_view(
            template_name='registration/registration_form.html',
            form_class=CustomEmailRegistrationForm,
            get_success_url=getattr(
                settings, 'REGISTRATION_EMAIL_REGISTER_SUCCESS_URL',
                lambda request, user: '/'),
        ),
        name='registration_register',
    ),
    url(r'^accounts/', include('registration_email.backends.default.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
