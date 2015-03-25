from django.conf.urls import patterns, include, url
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from .views import (HomePageView, OrganisationsView,
                    AllQuestionsView, AllAnswersView, OrganisationDetailView, AddQuestion)

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^organisations/', OrganisationsView.as_view(), name='organisations'),
    url(r'^organisation/(?P<pk>\d+)$', OrganisationDetailView.as_view(), name='organisation'),
    url(r'^organisation/(?P<org>\d+)/add_question$', require_POST(AddQuestion.as_view()), name='add_question'),
    url(r'^questions/all/', AllQuestionsView.as_view(), name='all_questions'),
    url(r'^answers/all/', AllAnswersView.as_view(), name='all_answers'),
)
