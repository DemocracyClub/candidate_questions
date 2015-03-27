from django.db import models
from token_auth.models import TokenAuthModel
from django.core.urlresolvers import reverse

class Candidate(TokenAuthModel):
    popit_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    contact_address = models.CharField(null=True, blank=True, max_length=255)
    constituency_id = models.CharField(max_length=20)
    constituency_name = models.CharField(max_length=64)
    party = models.CharField(max_length=64, null=True)
    participating = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def get_questions_url(self):
        return reverse('candidate_questions', kwargs={'pk': self.popit_id})
