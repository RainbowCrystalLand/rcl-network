# -*- coding: utf-8 -*-


from pybb.views import AddPostView, PostEditMixin
from pybb.permissions import perms

from pybb_custom.forms import CustomAdminPostForm, CustomPostForm

from django import forms

#class CustomPostEditMixin(PostEditMixin):


class CustomAddPostView(AddPostView):
	def get_form_class(self):
		print 'Custom!'
		if perms.may_post_as_admin(self.request.user):
			print 'returning Admin!'
			return CustomAdminPostForm
		else:
			return CustomPostForm
