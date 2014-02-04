# -*- coding: utf-8 -*-

from __future__ import unicode_literals
try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url

from django.contrib.auth.decorators import login_required

from pybb_custom.views import CustomAddPostView, CustomProfileEditView

from pybb.feeds import LastPosts, LastTopics
from pybb.views import IndexView, CategoryView, ForumView, TopicView,\
    EditPostView, UserView, PostView, \
    DeletePostView, StickTopicView, UnstickTopicView, CloseTopicView,\
    OpenTopicView, ModeratePost, TopicPollVoteView, LatestTopicsView,\
    UserTopics, UserPosts, topic_cancel_poll_vote


urlpatterns = patterns('',
                       # Syndication feeds
                       url('^feeds/posts/$', LastPosts(), name='feed_posts'),
                       url('^feeds/topics/$', LastTopics(), name='feed_topics'),
                       )

urlpatterns += patterns('pybb.views',
                        # Index, Category, Forum
                        url('^$', login_required(IndexView.as_view()), name='index'),
                        url('^category/(?P<pk>\d+)/$', login_required(CategoryView.as_view()), name='category'),
                        url('^forum/(?P<pk>\d+)/$', login_required(ForumView.as_view()), name='forum'),

                        # User
                        url('^users/(?P<username>[^/]+)/$', login_required(UserView.as_view()), name='user'),
                        url('^block_user/([^/]+)/$', 'block_user', name='block_user'),
                        url('^unblock_user/([^/]+)/$', 'unblock_user', name='unblock_user'),
                        url(r'^users/(?P<username>[^/]+)/topics/$', login_required(UserTopics.as_view()), name='user_topics'),
                        url(r'^users/(?P<username>[^/]+)/posts/$', login_required(UserPosts.as_view()), name='user_posts'),

                        # Profile
                        url('^profile/edit/$', login_required(CustomProfileEditView.as_view()), name='edit_profile'),

                        # Topic
                        url('^topic/(?P<pk>\d+)/$', login_required(TopicView.as_view()), name='topic'),
                        url('^topic/(?P<pk>\d+)/stick/$', login_required(StickTopicView.as_view()), name='stick_topic'),
                        url('^topic/(?P<pk>\d+)/unstick/$', login_required(UnstickTopicView.as_view()), name='unstick_topic'),
                        url('^topic/(?P<pk>\d+)/close/$', login_required(CloseTopicView.as_view()), name='close_topic'),
                        url('^topic/(?P<pk>\d+)/open/$', login_required(OpenTopicView.as_view()), name='open_topic'),
                        url('^topic/(?P<pk>\d+)/poll_vote/$', login_required(TopicPollVoteView.as_view()), name='topic_poll_vote'),
                        url('^topic/(?P<pk>\d+)/cancel_poll_vote/$', topic_cancel_poll_vote, name='topic_cancel_poll_vote'),
                        url('^topic/latest/$', login_required(LatestTopicsView.as_view()), name='topic_latest'),

                        # Add topic/post
                        url('^forum/(?P<forum_id>\d+)/topic/add/$', login_required(CustomAddPostView.as_view()), name='add_topic'),
                        url('^topic/(?P<topic_id>\d+)/post/add/$', login_required(CustomAddPostView.as_view()), name='add_post'),

                        # Post
                        url('^post/(?P<pk>\d+)/$', login_required(PostView.as_view()), name='post'),
                        url('^post/(?P<pk>\d+)/edit/$', login_required(EditPostView.as_view()), name='edit_post'),
                        url('^post/(?P<pk>\d+)/delete/$', login_required(DeletePostView.as_view()), name='delete_post'),
                        url('^post/(?P<pk>\d+)/moderate/$', login_required(ModeratePost.as_view()), name='moderate_post'),

                        # Attachment
                        #url('^attachment/(\w+)/$', 'show_attachment', name='pybb_attachment'),

                        # Subscription
                        url('^subscription/topic/(\d+)/delete/$',
                            'delete_subscription', name='delete_subscription'),
                        url('^subscription/topic/(\d+)/add/$',
                            'add_subscription', name='add_subscription'),

                        # API
                        url('^api/post_ajax_preview/$', 'post_ajax_preview', name='post_ajax_preview'),

                        # Commands
                        url('^mark_all_as_read/$', 'mark_all_as_read', name='mark_all_as_read')
                        )
