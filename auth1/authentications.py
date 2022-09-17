from typing import Union

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import authentication, exceptions
from rest_framework.authentication import get_authorization_header

from .schema import DataAccessModel
from .settings import AUTH1_USER_ID_FIELD

User = get_user_model()


class TokenAuthentication(DataAccessModel, authentication.BaseAuthentication):
    keyword = 'Bearer'

    def authenticate_header(self, request):
        return self.keyword

    def authenticate(self, request):
        _user_token = self.get_token(request)

        if _user_token is None:
            # skip this authentication for next backend
            return None

        _user_id = self.get_user_id(_user_token)
        _user = self.get_user(_user_id)
        self.check_user(_user)
        return _user, _user_token

    def get_token(self, request) -> Union[str, None]:
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return token

    def get_user_id(self, access_token):
        _user_id = self.cache.get(self.access_token_key(access_token))
        if _user_id:
            return _user_id

        raise exceptions.AuthenticationFailed(_('Invalid or Expired token.'))

    def get_user(self, user_id):
        q = {
            AUTH1_USER_ID_FIELD: user_id,
        }

        if User.objects.filter(**q).exists():
            _user = User.objects.get(**q)
            return _user

        raise exceptions.AuthenticationFailed(_('User not found.'))

    def check_user(self, user):
        if not user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))
