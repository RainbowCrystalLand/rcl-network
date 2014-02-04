# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from pybb import defaults

__author__ = 'zeus'


def processor(request):
    context = {}
    for i in (
        'PYBB_TEMPLATE',
        'PYBB_DEFAULT_AVATAR_URL',
        'PYBB_MARKUP',
        'PYBB_DEFAULT_TITLE',
        'PYBB_ENABLE_ANONYMOUS_POST',
        'PYBB_ATTACHMENT_ENABLE', # deprecated, should be used pybb_may_attach_files filter, will be removed
        'PYBB_AVATAR_WIDTH',
        'PYBB_AVATAR_HEIGHT',
        'PYBB_ATTACHMENT_SIZE_LIMIT',
    ):
        context[i] = getattr(defaults, i, None)
    context['PYBB_AVATAR_DIMENSIONS'] = '%sx%s' % (defaults.PYBB_AVATAR_WIDTH, defaults.PYBB_AVATAR_WIDTH)
    
    context['PYBB_ATTACHMENT_SIZE_LIMIT_MB'] = context['PYBB_ATTACHMENT_SIZE_LIMIT']/1024/1024
    
    return context
