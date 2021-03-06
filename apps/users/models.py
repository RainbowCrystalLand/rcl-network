# -*- coding: utf-8 -*-

import warnings
from django.db import models
# models
from django.contrib.auth.models import (UserManager, AbstractBaseUser, PermissionsMixin)
# exceptions
from django.contrib.auth.models import SiteProfileNotAvailable
from django.core.exceptions import ImproperlyConfigured
# translation & other utils
from django.utils.translation import ugettext_lazy as _
from django.utils.http import urlquote
from django.core.mail import send_mail
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    """
    Our custom User model. Represents a physical person that users the
    network.
    """
    ## FIELDS ##
    username = models.CharField(_('nickname'), max_length=64,
        help_text=_('How do people call you?'), default='', 
        blank=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(
        _('staff status'), default=False, help_text=_(
            'Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(
        _('active'), default=True, help_text=_(
            'Designates whether this user should be treated as '
            'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    biography = models.TextField(_('biography'), 
        help_text=_('Let others know a bit about you'), blank=True)

    ## Managers ##
    objects = UserManager()

    ## CONSTANTS ##
    # we use the email as identifier, check
    # https://docs.djangoproject.com/en/dev/topics/auth/customizing
    # /#django.contrib.auth.models.CustomUser.USERNAME_FIELD
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    ## CLASSES AND METHODS ##
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.pk)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def get_profile(self):
        """
        Returns site-specific profile for this user. Raises
        SiteProfileNotAvailable if this site does not allow profiles.
        """
        warnings.warn(
            "The use of AUTH_PROFILE_MODULE to define user "
            "profiles has been deprecated.",
            PendingDeprecationWarning)
        if not hasattr(self, '_profile_cache'):
            from django.conf import settings
            if not getattr(settings, 'AUTH_PROFILE_MODULE', False):
                raise SiteProfileNotAvailable(
                    'You need to set AUTH_PROFILE_MODULE in your project '
                    'settings')
            try:
                app_label, model_name = settings.AUTH_PROFILE_MODULE.split('.')
            except ValueError:
                raise SiteProfileNotAvailable(
                    'app_label and model_name should be separated by a dot in '
                    'the AUTH_PROFILE_MODULE setting')
            try:
                model = models.get_model(app_label, model_name)
                if model is None:
                    raise SiteProfileNotAvailable(
                        'Unable to load the profile model, check '
                        'AUTH_PROFILE_MODULE in your project settings')
                self._profile_cache = model._default_manager.using(
                    self._state.db).get(user__id__exact=self.id)
                self._profile_cache.user = self
            except (ImportError, ImproperlyConfigured):
                raise SiteProfileNotAvailable
        return self._profile_cache
