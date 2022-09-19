import secrets
from datetime import timedelta

from django.utils import timezone

from .schema import DataAccessModel
from .settings import (
    AUTH1_ACCESS_TOKEN_EXPIRATION,
    AUTH1_REFRESH_TOKEN_EXPIRATION,
    AUTH1_USER_ID_FIELD
)


# TODO: create ORM class for cache
# TODO: i think we cant pass top level object like user to this class
class SimpleToken(DataAccessModel):
    def random(self, length=32) -> str:
        return secrets.token_hex(length)

    def timedelta(self, seconds: int) -> timedelta:
        return timezone.now() + timedelta(seconds=seconds)

    def generate(self, user) -> dict:
        _access_token = self.random()
        _refresh_token = self.random()

        # FIXME: i think we can only create + validate token at this class
        _access_token_expiration = self.timedelta(AUTH1_ACCESS_TOKEN_EXPIRATION)
        _refresh_token_expiration = self.timedelta(AUTH1_REFRESH_TOKEN_EXPIRATION)

        self.set_access_token(user, _access_token, AUTH1_ACCESS_TOKEN_EXPIRATION)
        self.set_refresh_token(user, _refresh_token, AUTH1_REFRESH_TOKEN_EXPIRATION)

        return {
            'access_token': _access_token,
            'refresh_token': _refresh_token,
            'access_token_expiration': _access_token_expiration,
            'refresh_token_expiration': _refresh_token_expiration,
        }

    def revoke(self, access_token, refresh_token) -> dict:
        self.revoke_access_token(access_token)
        self.revoke_refresh_token(refresh_token)

        return {'success': True}

    def verify(self, access_token=None, refresh_token=None) -> dict:
        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }


class JWTToken:
    pass


class HMACToken:
    pass
