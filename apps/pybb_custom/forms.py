# -*- coding: utf-8 -*-

# forms
from pybb.forms import PostForm, AdminPostForm, EditProfileForm
# models
from pybb.models import Post
# translation & other utils
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from pybb import util

from settings import CRISPY_TEMPLATE_PACK


class Bootstrap3HorizontalHelper(FormHelper):
	def __init__(self, *args, **kwargs):
		super(Bootstrap3HorizontalHelper, self).__init__(*args, **kwargs)
		self.form_class = 'form-horizontal'
		self.label_class = 'col-lg-2'
		self.field_class = 'col-lg-8'


class CustomAdminPostForm(AdminPostForm):
	def __init__(self, *args, **kwargs):
		super(CustomAdminPostForm, self).__init__(*args, **kwargs)
		self.helper = Bootstrap3HorizontalHelper(self)
		self.helper.template = '%s/uni_form.html' % CRISPY_TEMPLATE_PACK

	class Meta(object):
		model = Post
		fields = ['name', 'body']


class CustomPostForm(PostForm):
	def __init__(self, *args, **kwargs):
		super(CustomPostForm, self).__init__(*args, **kwargs)
		self.helper = Bootstrap3HorizontalHelper(self)
		self.helper.template = '%s/uni_form.html' % CRISPY_TEMPLATE_PACK
		self.helper.layout = Layout(
		    'name',
		    'body',
		)

	class Meta(object):
		model = Post
		fields = ['name', 'body']


class CustomEditProfileForm(EditProfileForm):
	def __init__(self, *args, **kwargs):
		super(CustomEditProfileForm, self).__init__(*args, **kwargs)
		self.helper = Bootstrap3HorizontalHelper(self)
		self.helper.template = '%s/uni_form.html' % CRISPY_TEMPLATE_PACK
		self.helper.add_input(Submit('save', _('Save')))

	class Meta(object):
            model = util.get_pybb_profile_model()
            fields = ['avatar', 'signature', 'show_signatures']
