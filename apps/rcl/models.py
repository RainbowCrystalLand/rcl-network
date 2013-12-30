from django.db import models
# translation & other utils
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


class RCL(models.Model):
    ## FIELDS ##
    name = models.CharField(_('name'), max_length=255)
    location = models.TextField(_('location'))
    description = models.TextField(_('description'))
    internet_focalizer = models.ForeignKey(
        get_user_model(), verbose_name=_('internet focalizer'), null=True,
        related_name='focalized_rcl')
    observer = models.ForeignKey(
        get_user_model(), verbose_name=_('observer'), null=True,
        related_name='observer_rcl')
    privacy_settings = models.OneToOneField(
        'privacy.RCLPrivacySetting', verbose_name=_('privacy settings'),
        null=True, blank=True)

    ## META ##
    class Meta:
        abstract = True


class Community(RCL):
    ## CONSTANTS ##
    LAND = 'land'
    APP = 'appartment'
    KIND_CHOICES = (
        (LAND, _('land')),
        (APP, _('appartment'))
    )

    ## FIELDS ##
    kind = models.CharField(_('kind'), max_length=15, choices=KIND_CHOICES)
    max_capacity = models.PositiveIntegerField(_('max capacity'), null=True)
    current_residents_amount = models.PositiveIntegerField(
        _('number of current residents'), null=True)
    needs_people = models.BooleanField(_('needs people'), default=False)
    url_name = models.SlugField(
        _('url name'), max_length=127, unique=True, db_index=True)
    datetime_joined = models.DateTimeField(_('datetime joined'), auto_now_add=True)

    ## METHODS ##
    def __unicode__(self):
        return u'%s' % self.name


class CommunityExperience(models.Model):
    ## FIELDS ##
    user = models.ForeignKey(
        get_user_model(), verbose_name=_('user'),
        related_name='community_experiences')
    community = models.ForeignKey(
        Community, verbose_name=_('community'),
        related_name='user_experiences')
    rating = models.PositiveSmallIntegerField(_('rating'), default=0)
    comment = models.TextField(_('comment'))
