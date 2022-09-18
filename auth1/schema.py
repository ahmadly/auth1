from django.core.cache import caches

from .settings import (
    AUTH1_KEY_PREFIX,
    AUTH1_TOKEN_CACHE_ALIAS,
    AUTH1_USER_ID_FIELD
)

cache = caches[AUTH1_TOKEN_CACHE_ALIAS]


def prefixed_key(f):
    """
    A method decorator that prefixes return values.

    Prefixes any string that the decorated method `f` returns with the value of
    the `prefix` attribute on the owner object `self`.
    """

    def prefixed_method(self, *args, **kwargs):
        key = f(self, *args, **kwargs)
        return f"{self.prefix}:{key}"

    return prefixed_method


class DataAccessModel:
    """
    Methods to generate key names for cache data structures.

    These key names are used by the DAO classes. This class therefore contains
    a reference to all possible key names used by this application.
    """

    def __init__(self, prefix: str = None):
        if prefix is None:
            prefix = AUTH1_KEY_PREFIX
        self.prefix = prefix
        self.cache = cache

    @prefixed_key
    def access_token_key(self, access_token: str) -> str:
        return f"access_tokens:{access_token}"

    @prefixed_key
    def refresh_token_key(self, refresh_token: str) -> str:
        return f"refresh_tokens:{refresh_token}"

    @prefixed_key
    def user_session_key(self, user_id: int) -> str:
        return f"user_sessions:{user_id}"

    @prefixed_key
    def login_counter_key(self, user_id: int):
        return f"login_counter:{user_id}"

    def set(self, key: str, value, timeout: int = None) -> None:
        self.cache.set(key, value, timeout)

    def get(self, key: str):
        return self.cache.get(key)

    def set_access_token(self, user, access_token, access_token_expiration):
        access_key = self.access_token_key(access_token)
        self.cache.set(access_key, getattr(user, AUTH1_USER_ID_FIELD), access_token_expiration)

    def set_refresh_token(self, user, refresh_token, refresh_token_expiration):
        refresh_key = self.refresh_token_key(refresh_token)
        self.cache.set(refresh_key, getattr(user, AUTH1_USER_ID_FIELD), refresh_token_expiration)

    def revoke_access_token(self, access_token):
        access_key = self.access_token_key(access_token)
        self.cache.delete(access_key)

    def revoke_refresh_token(self, refresh_token):
        refresh_key = self.refresh_token_key(refresh_token)
        self.cache.delete(refresh_key)
