from django.conf.urls import patterns, url
from users.views import UserUpdateView

urlpatterns = patterns('',
    url(r'^profile/edit/$', UserUpdateView.as_view(),
        name='users-information-edit'),
)
