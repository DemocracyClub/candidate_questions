# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from tastypie.api import Api
from questions.api.resources import AnswerResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(AnswerResource())

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^organisations', include('organisations.urls')),
    url(r'^candidates', include('candidates.urls')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    # url(r'^', include('prototype.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
