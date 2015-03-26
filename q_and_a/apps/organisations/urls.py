from django.conf.urls import patterns, url
from django.views.decorators.http import require_POST

from .views import OrganisationAuthenticateView, QuestionAdminView, OrganisationDetailView, OrganisationListView
from questions.views import AddQuestion

urlpatterns = patterns('',
    url(r'^/$', OrganisationListView.as_view(), name='organisations'),
    url(r'^/authenticate/(?P<token>.*)/',
        OrganisationAuthenticateView.as_view(),
        name='organisations_authenticate'),
    url(r'^/questions/', QuestionAdminView.as_view(),
        name='organisation_questions'),
    url(r'^/(?P<pk>\d+)/?$', OrganisationDetailView.as_view(), name='organisation'),
    url(r'^/(?P<org>\d+)/add_question$', require_POST(AddQuestion.as_view()), name='add_question'),
)
