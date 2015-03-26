from django.views.generic import RedirectView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth import login, authenticate
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse

class BaseAuthView(SingleObjectMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        if (not self.request.user.is_authenticated()
                and not hasattr(self.request.user, 'organisation_id')):
            auth_user = authenticate(auth_token=self.kwargs['token'])
            if not auth_user:
                raise PermissionDenied()
            login(self.request, auth_user)
        return reverse('organisation_questions')
