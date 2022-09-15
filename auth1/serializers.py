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

token_class = import_string(settings.REST_FRAMEWORK['TOKEN_CLASS'])


class LoginSerializer(serializers.Serializer):
    username = UsernameField()
    password = PasswordField()

    def validate(self, attrs: dict) -> dict:
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError('Invalid username/password')

        return self.get_token(user)

    def get_token(self, user) -> dict:
        return token_class().generate(user)


class LogoutSerializer(serializers.Serializer):
    # TODO: do we need both token and refresh_token?
    access_token = AccessTokenField()
    refresh_token = RefreshTokenField()

    def validate(self, attrs: dict) -> dict:
        access_token = attrs.get('access_token')
        refresh_token = attrs.get('refresh_token')

        token_class().revoke(access_token, refresh_token)

        return {'success': True}


class VerifySerializer(serializers.Serializer):
    pass


class RefreshSerializer(serializers.Serializer):
    pass


class RegisterSerializer(serializers.Serializer):
    pass


class ConfirmSerializer(serializers.Serializer):
    pass


class BlockSerializer(serializers.Serializer):
    pass
