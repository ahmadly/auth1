import secrets
from datetime import timedelta

from django.conf import settings
from django.core.cache import caches
from django.utils import timezone

cache = caches[settings.REST_FRAMEWORK['TOKEN_CACHE_ALIAS']]
user_id_field = settings.REST_FRAMEWORK['USER_ID_FIELD']

access_token_expiration = settings.REST_FRAMEWORK['ACCESS_TOKEN_EXPIRATION']
refresh_token_expiration = settings.REST_FRAMEWORK['REFRESH_TOKEN_EXPIRATION']


# TODO: create ORM class for cache
class SimpleToken:
    def generate(self, user) -> dict:
        _access_token = secrets.token_hex(32)
        _refresh_token = secrets.token_hex(32)
        _access_token_expiration = timezone.now() + timedelta(seconds=access_token_expiration)
        _refresh_token_expiration = timezone.now() + timedelta(seconds=refresh_token_expiration)

        cache.set(_access_token, getattr(user, user_id_field), access_token_expiration)
        cache.set(_refresh_token, getattr(user, user_id_field), refresh_token_expiration)

        # TODO: handle single session
        return {
            'access_token': _access_token,
            'refresh_token': _refresh_token,
            'access_token_expiration': _access_token_expiration,
            'refresh_token_expiration': _refresh_token_expiration,
        }

    def revoke(self, access_token, refresh_token) -> None:
        cache.delete(access_token)
        cache.delete(refresh_token)


class JWTToken:
    pass
