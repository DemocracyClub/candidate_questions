from django.views.generic import RedirectView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth import login, authenticate
from django.core.exceptions import PermissionDenied

class BaseAuthView(SingleObjectMixin, RedirectView):
    def login(self):
        auth_user = authenticate(auth_token=self.kwargs['token'])
        if not auth_user:
            raise PermissionDenied()
        login(self.request, auth_user)


