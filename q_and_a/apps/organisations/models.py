from django.db import models

from token_auth.models import TokenAuthModel


class Organisation(TokenAuthModel):
    name = models.CharField(blank=False, max_length=255)
