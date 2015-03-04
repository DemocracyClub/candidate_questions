from django.test import TestCase

from organisations.models import Organisation

class TestOrganisationModels(TestCase):
    def test_model_creation(self):
        """
        More of a smoke test for the model creation
        """
        o = Organisation(name="test")
        o.save()
        self.assertTrue(bool(o.created))
        self.assertEqual(o.name, "test")
        self.assertTrue(o.auth_token)