from token_auth.authentication import BaseTokenAuthBackend

from .models import Organisation

class OrganisationTokenAuthBackend(BaseTokenAuthBackend):
    model_class = Organisation
