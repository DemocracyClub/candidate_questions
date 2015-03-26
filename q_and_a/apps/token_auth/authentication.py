from django.contrib.auth.models import User


class BaseTokenAuthBackend(object):
    def authenticate(self, auth_token):
        try:
            model = self.model_class.objects.get(auth_token=auth_token)
        except self.model_class.DoesNotExist:
            return None
        return model.user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
