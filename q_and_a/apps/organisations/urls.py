from django.conf.urls import patterns, include, url


from .views import (OrganisationAuthenticateView, QuestionAdminView)

urlpatterns = patterns('',
    url(r'^/authenticate/(?P<token>.*)/',
        OrganisationAuthenticateView.as_view(),
        name='organisations_authenticate'),
    url(r'^/questions/', QuestionAdminView.as_view(),
        name='organisation_questions'),
)
