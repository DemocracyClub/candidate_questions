from django.db import models
from token_auth.models import TokenAuthModel

class Candidate(TokenAuthModel):
    popit_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    contact_address = models.CharField(null=True, blank=True, max_length=255)
    constituency_id = models.CharField(max_length=20)
    constituency_name = models.CharField(max_length=64)
    party = models.CharField(max_length=64, null=True)

    def __unicode__(self):
        return self.name

