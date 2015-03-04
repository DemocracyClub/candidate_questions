import binascii
import os

from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

from .models import TokenAuthModel





class TokenAuth(AppConfig):
    name = 'token_auth'
    verbose_name = "Token Authentication"


