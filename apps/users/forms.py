# -*- coding: utf-8 -*-

from django.forms import ModelForm
# models
from users.models import User


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'biography')
