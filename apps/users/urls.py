from django.conf.urls import patterns, url
from users.views import UserUpdateView, DashboardView
# decorators
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^dashboard/$', login_required(DashboardView.as_view()),
        name='users-dashboard'),
    url(r'^profile/edit/$', login_required(UserUpdateView.as_view()),
        name='users-profile-edit'),
)
