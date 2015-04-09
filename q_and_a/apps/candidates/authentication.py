from token_auth.authentication import BaseTokenAuthBackend

from .models import Candidate

class CandidateTokenAuthBackend(BaseTokenAuthBackend):
    model_class = Candidate
