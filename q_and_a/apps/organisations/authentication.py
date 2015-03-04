from token_auth.authentication import BaseTokenAuthBackend

from .models import Organisation

class OrginaisationTokenAuthBackend(BaseTokenAuthBackend):
    model_class = Organisation