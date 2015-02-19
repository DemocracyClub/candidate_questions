from django.conf.urls import patterns, include, url

from .views import (HomePageView, OrganisationsView,
                    AllQuestionsView, AllAnswersView)

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^organisations/', OrganisationsView.as_view(), name='organisations'),
    url(r'^questions/all/', AllQuestionsView.as_view(), name='all_questions'),
    url(r'^answers/all/', AllAnswersView.as_view(), name='all_answers'),
)