# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

from custom_registration.forms import CustomEmailRegistrationForm
from custom_registration.backends import CustomRegistrationView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='rcl/main/home.html'), name='home'),
    url(r'^rcl/', include('rcl.urls', namespace='rcl')),
    url(r'^u/', include('users.urls', namespace='users')),
    
    # Overrides to fix an error when using the User's email to login
    # and to protect views with "login_required"
    url(r'^forum/', include('pybb_custom.urls', namespace='pybb')),

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
    # These below fix a problem with django_registration
    url(r'^password/reset/$',
        auth_views.password_reset,
        name='password_reset'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^password/reset/complete/$',
        auth_views.password_reset_complete,
        name='password_reset_complete'),
    url(r'^password/reset/done/$',
        auth_views.password_reset_done,
        name='password_reset_done'),
    url(r'^accounts/', include('registration_email.backends.default.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
