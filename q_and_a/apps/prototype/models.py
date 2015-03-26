from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=128)
    contact_address = models.CharField(null=True, blank=True, max_length=255)
    popit_url = models.CharField(max_length=255, unique=True)
    constituency_id = models.CharField(max_length=20)
    constituency_name = models.CharField(max_length=64)
    party = models.CharField(max_length=64, null=True)
