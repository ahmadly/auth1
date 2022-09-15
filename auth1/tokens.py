import secrets
from datetime import timedelta

from django.conf import settings
from django.utils import timezone

from .schema import DataAccessModel

user_id_field = settings.REST_FRAMEWORK['USER_ID_FIELD']

access_token_expiration = settings.REST_FRAMEWORK['ACCESS_TOKEN_EXPIRATION']
refresh_token_expiration = settings.REST_FRAMEWORK['REFRESH_TOKEN_EXPIRATION']


# TODO: create ORM class for cache
class SimpleToken(DataAccessModel):
    def random(self, length=32) -> str:
        return secrets.token_hex(length)

    def timedelta(self, seconds: int) -> timedelta:
        return timezone.now() + timedelta(seconds=seconds)

    def generate(self, user) -> dict:
        _access_token = self.random()
        _refresh_token = self.random()
        _access_token_expiration = self.timedelta(access_token_expiration)
        _refresh_token_expiration = self.timedelta(refresh_token_expiration)

        self.set_access_token(user, _access_token, access_token_expiration)
        self.set_refresh_token(user, _refresh_token, refresh_token_expiration)

        return {
            'access_token': _access_token,
            'refresh_token': _refresh_token,
            'access_token_expiration': _access_token_expiration,
            'refresh_token_expiration': _refresh_token_expiration,
        }

    def revoke(self, access_token, refresh_token) -> None:
        self.revoke_access_token(access_token)
        self.revoke_refresh_token(refresh_token)


class JWTToken:
    pass
