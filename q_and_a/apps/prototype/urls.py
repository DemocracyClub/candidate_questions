from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from .views import (HomePageView, OrganisationsView,
                    AllQuestionsView, AllAnswersView)

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^organisations/', OrganisationsView.as_view(), name='organisations'),
    url(r'^questions/all/', AllQuestionsView.as_view(), name='all_questions'),
    url(r'^answers/all/', AllAnswersView.as_view(), name='all_answers'),
)