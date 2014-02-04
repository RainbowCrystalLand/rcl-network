from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
 

urlpatterns = patterns('',
    # Fill with URLs for Rainbow Crystal Lands main page and minipages
    url(r'^history/$', TemplateView.as_view(template_name='rcl/main/history.html'), 
    	name='main-history'),
    url(r'^dci/$', TemplateView.as_view(template_name='rcl/main/dci.html'), 
    	name='main-dci'),
    url(r'^join/$', TemplateView.as_view(template_name='rcl/main/join.html'), 
    	name='main-join'),
    url(r'^faq/$', TemplateView.as_view(template_name='rcl/main/faq.html'), 
        name='main-faq'),
    url(r'^donate/$', TemplateView.as_view(template_name='rcl/main/donate.html'), 
    	name='main-donate'),
    url(r'^vision-explained/$', TemplateView.as_view(template_name='rcl/main/vision_explained.html'), 
    	name='main-vision-explained'),
    url(r'^about/$', TemplateView.as_view(template_name='rcl/main/about.html'), 
    	name='main-about'),
    url(r'^activate/$', TemplateView.as_view(
    	template_name='rcl/main/registration_successful.html'), 
    	name='main-registration-successful'),
    # Welcome after activation
    url(r'^welcome/$', TemplateView.as_view(template_name='rcl/main/welcome.html'), 
        name='main-welcome'),
)
