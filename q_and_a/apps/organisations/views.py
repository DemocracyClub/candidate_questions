from django.views.generic import TemplateView

from braces.views import UserPassesTestMixin

from token_auth.views import BaseAuthView

class OrganisationAuthenticateView(BaseAuthView):
    pass

class QuestionAdminView(UserPassesTestMixin, TemplateView):
    template_name="organisations/questions/questions_admin.html"

    def test_func(self, user):
        return getattr(user, 'organisation', None)