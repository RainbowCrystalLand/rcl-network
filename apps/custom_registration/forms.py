# -*- coding: utf-8 -*-

from django import forms
# translation & other utils
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from registration_email.forms import EmailRegistrationForm

User = get_user_model()


class CustomEmailRegistrationForm(EmailRegistrationForm):
    username = forms.CharField(label=_('Nickname (optional)'), required=False,
        help_text=_("If you don't set a nickname the first part of your email \
            will be used"))

    class Meta:
        model = User
        fields = ('email', 'username',)

    def clean(self):
        """
        Verifiy that the values entered into the two password fields match.

        Note that an error here will end up in ``non_field_errors()`` because
        it doesn't apply to a single field.

        """
        data = self.cleaned_data
        if data.get('your_name'):
            # Bot protection. The name field is not visible for human users.
            raise forms.ValidationError(_('Please enter a valid name.'))
        if not 'email' in data:
            return data
        if ('password1' in data and 'password2' in data):

            if data['password1'] != data['password2']:
                raise forms.ValidationError(
                    _("The two password fields didn't match."))
        return self.cleaned_data
