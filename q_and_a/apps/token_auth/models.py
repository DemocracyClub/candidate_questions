from django.db import models
from django.contrib.auth.models import User

from django_extensions.db.models import TimeStampedModel


class TokenAuthModel(TimeStampedModel):
    auth_token = models.CharField(blank=True, max_length=255, db_index=True)
    user = models.OneToOneField(User)

    class Meta:
        abstract = True

    def generate_key():
        return binascii.hexlify(os.urandom(20)).decode()

    def save(self, *args, **kwargs):
        if not self.user_id:
            new_user = User()
            new_user.save()
            self.user = new_user

        if not self.auth_token:
            self.auth_token = self.generate_key()

        super(TokenAuthModel, self).save(*args, **kwargs)
