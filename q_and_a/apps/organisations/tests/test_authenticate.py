from django.contrib.auth import login, authenticate
from django.test import TestCase

from organisations.models import Organisation

def make_organisation(auth_token, name="test"):
    o = Organisation(name=name, auth_token=auth_token)
    o.save()

class TestOrganisationAuth(TestCase):
    def test_organisation_auth(self):
        """
        More of a smoke test for the model creation
        """
        make_organisation('111')
        auth_user = authenticate(auth_token="111")
        self.assertIsNotNone(auth_user)
        auth_user = authenticate(auth_token="WRONG")
        self.assertIsNone(auth_user)
