from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
# forms
from users.forms import UserUpdateForm
# models
from users.models import User
# translation & other utils
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


class DashboardView(TemplateView):
    template_name = 'users/dashboard.html'


class UserUpdateView(UpdateView):
    """
    Process the update of a user information.
    """
    form_class = UserUpdateForm
    template_name_suffix = '_update_form'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse('users-profile-edit')

    def form_valid(self, form):
        '''
        Sets the success message
        '''
        messages.success(self.request, _('Information successfully updated'))
        return super(UserUpdateView, self).form_valid(form)
