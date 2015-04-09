from django.views.generic import TemplateView, ListView, DetailView
from braces.views import UserPassesTestMixin
from token_auth.views import BaseAuthView
from .models import Organisation
from questions.forms import QuestionForm

class OrganisationAuthenticateView(BaseAuthView):
    def get_redirect_url(self, *args, **kwargs):
        if (not self.request.user.is_authenticated()
                and not hasattr(self.request.user, 'organisation_id')):
            self.login()
        return self.request.user.organisation.get_absolute_url()

class QuestionAdminView(UserPassesTestMixin, TemplateView):
    template_name = "organisations/questions/questions_admin.html"

    def test_func(self, user):
        return getattr(user, 'organisation', None)

class OrganisationListView(ListView):
    model = Organisation

class OrganisationDetailView(DetailView):
    model = Organisation

    def get_context_data(self, **kwargs):
        context = super(OrganisationDetailView, self).get_context_data(**kwargs)
        context['form'] = QuestionForm
        return context
