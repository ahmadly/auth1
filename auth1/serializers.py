from django.conf import settings
from django.contrib.auth import authenticate
from django.utils.module_loading import import_string
from rest_framework import serializers

from .fields import (
    AccessTokenField,
    PasswordField,
    RefreshTokenField,
    UsernameField
)
from .schema import DataAccessModel

from .settings import AUTH1_TOKEN, AUTH1_USER_ID_FIELD, AUTH1_COUNTER

TokenClass = import_string(AUTH1_TOKEN)


class LoginSerializer(DataAccessModel, serializers.Serializer):
    username = UsernameField()
    password = PasswordField()

    def validate(self, attrs: dict) -> dict:
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError('Invalid username/password')

        if AUTH1_COUNTER:
            self.cache.incr(self.login_counter_key(user.id))

        return self.get_token(user)

    def get_token(self, user) -> dict:
        return TokenClass().generate(user)


class LogoutSerializer(DataAccessModel, serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    # TODO: do we need both token and refresh_token?
    access_token = AccessTokenField()
    refresh_token = RefreshTokenField()

    def validate(self, attrs: dict) -> dict:
        access_token = attrs.get('access_token')
        refresh_token = attrs.get('refresh_token')
        user = attrs.get('user')

        if AUTH1_COUNTER:
            self.cache.decr(self.login_counter_key(user.id))

        return TokenClass().revoke(access_token, refresh_token)


class VerifySerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    access_token = AccessTokenField()
    refresh_token = RefreshTokenField()

    def validate(self, attrs: dict) -> dict:
        access_token = attrs.get('access_token')
        refresh_token = attrs.get('refresh_token')
        user = attrs.get('user')

        data: dict = TokenClass().verify(access_token, refresh_token)
        data.update({'success': True, AUTH1_USER_ID_FIELD: getattr(user, AUTH1_USER_ID_FIELD)})
        return data


class RefreshSerializer(serializers.Serializer):
    pass


class RegisterSerializer(serializers.Serializer):
    pass


class ConfirmSerializer(serializers.Serializer):
    pass


class BlockSerializer(serializers.Serializer):
    pass


class ProfileSerializer(serializers.Serializer):
    pass
