from django.db import models
from token_auth.models import TokenAuthModel
from django.core.urlresolvers import reverse

class Organisation(TokenAuthModel):
    name = models.CharField(blank=False, max_length=255)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('organisation', kwargs={'pk': self.id})
