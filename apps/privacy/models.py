from django.db import models
# translation & other utils
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


class PrivacyLevel(models.Model):
    ## FIELDS ##
    name = models.CharField(_('name'), max_length=31)
    level = models.PositiveIntegerField(
        _('level'), unique=True,
        help_text=_('this is the access level, the highest the '
                    'number the more access level will need users '
                    'to see components with this privacy level'))
    creator = models.ForeignKey(
        get_user_model(), verbose_name=_('creator'), blank=True)
    datetime_created = models.DateTimeField(
        _('creation datetime'), auto_now_add=True, blank=True)

    ## METHODS ##
    def __unicode__(self):
        return u'%s' % self.name


class RCLPrivacySetting(models.Model):
    '''
    This model holds all the privacy settings that RCLs can make to their
    mini site in order to show more or show less information. Only users with
    an access level equal or greater thatn required should access to content.

    If a component has NULL privacy level value, then it's public.
    '''

    ## FIELDS ##
    location_privacy = models.ForeignKey(
        PrivacyLevel, verbose_name=_('location privacy'),
        related_name='location_settings_applied', null=True)
    photos_privacy = models.ForeignKey(
        PrivacyLevel, verbose_name=_('photos privacy'),
        related_name='photos_settings_applied', null=True)
    residents_privacy = models.ForeignKey(
        PrivacyLevel, verbose_name=_('residents privacy'),
        related_name='residents_settings_applied', null=True)
    calendar_privacy = models.ForeignKey(
        PrivacyLevel, verbose_name=_('calendar privacy'),
        related_name='calendar_settings_applied', null=True)
    projects_privacy = models.ForeignKey(
        PrivacyLevel, verbose_name=_('projects privacy'),
        related_name='projects_settings_applied', null=True)
    experiences_privacy = models.ForeignKey(
        PrivacyLevel, verbose_name=_('experiences privacy'),
        related_name='exoeriences_settings_applied', null=True)
    donations_privacy = models.ForeignKey(
        PrivacyLevel, verbose_name=_('donations privacy'),
        related_name='donations_settings_applied', null=True)
