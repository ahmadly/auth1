from django.conf import settings

AUTH1_VIEWS_LOGIN = getattr(settings, 'AUTH1_VIEWS_LOGIN', 'auth1.views.LoginView')
AUTH1_VIEWS_LOGOUT = getattr(settings, 'AUTH1_VIEWS_LOGOUT', 'auth1.views.LogoutView')
AUTH1_VIEWS_VERIFY = getattr(settings, 'AUTH1_VIEWS_VERIFY', 'auth1.views.VerifyView')
AUTH1_VIEWS_REFRESH = getattr(settings, 'AUTH1_VIEWS_REFRESH', 'auth1.views.RefreshView')
AUTH1_VIEWS_REGISTER = getattr(settings, 'AUTH1_VIEWS_REGISTER', 'auth1.views.RegisterView')
AUTH1_VIEWS_CONFIRM = getattr(settings, 'AUTH1_VIEWS_CONFIRM', 'auth1.views.ConfirmView')
AUTH1_VIEWS_BLOCK = getattr(settings, 'AUTH1_VIEWS_BLOCK', 'auth1.views.BlockView')
AUTH1_VIEWS_PROFILE = getattr(settings, 'AUTH1_VIEWS_PROFILE', 'auth1.views.ProfileView')

AUTH1_SERIALIZERS_LOGIN = getattr(settings, 'AUTH1_SERIALIZERS_LOGIN', 'auth1.serializers.LoginSerializer')
AUTH1_SERIALIZERS_LOGOUT = getattr(settings, 'AUTH1_SERIALIZERS_LOGOUT', 'auth1.serializers.LogoutSerializer')
AUTH1_SERIALIZERS_VERIFY = getattr(settings, 'AUTH1_SERIALIZERS_VERIFY', 'auth1.serializers.VerifySerializer')
AUTH1_SERIALIZERS_REFRESH = getattr(settings, 'AUTH1_SERIALIZERS_REFRESH', 'auth1.serializers.RefreshSerializer')
AUTH1_SERIALIZERS_REGISTER = getattr(settings, 'AUTH1_SERIALIZERS_REGISTER', 'auth1.serializers.RegisterSerializer')
AUTH1_SERIALIZERS_CONFIRM = getattr(settings, 'AUTH1_SERIALIZERS_CONFIRM', 'auth1.serializers.ConfirmSerializer')
AUTH1_SERIALIZERS_BLOCK = getattr(settings, 'AUTH1_SERIALIZERS_BLOCK', 'auth1.serializers.BlockSerializer')
AUTH1_SERIALIZERS_PROFILE = getattr(settings, 'AUTH1_SERIALIZERS_PROFILE', 'auth1.serializers.ProfileSerializer')

AUTH1_TOKEN_CACHE_ALIAS = getattr(settings, 'AUTH1_TOKEN_CACHE_ALIAS', 'default')

AUTH1_TOKEN = getattr(settings, 'AUTH1_TOKEN', 'auth1.tokens.SimpleToken')

AUTH1_ACCESS_TOKEN_EXPIRATION = getattr(settings, 'AUTH1_ACCESS_TOKEN_EXPIRATION', 1 * 60 * 60)  # 1 hours
AUTH1_REFRESH_TOKEN_EXPIRATION = getattr(settings, 'AUTH1_REFRESH_TOKEN_EXPIRATION', 24 * 60 * 60)  # 24 hours

AUTH1_USER_SELECT_RELATED = getattr(settings, 'AUTH1_USER_SELECT_RELATED', [])
AUTH1_USER_PREFETCH_RELATED = getattr(settings, 'AUTH1_USER_PREFETCH_RELATED', [])
AUTH1_USER_ID_FIELD = getattr(settings, 'AUTH1_USER_ID_FIELD', 'id')
AUTH1_USER_NAME_FIELD = getattr(settings, 'AUTH1_USER_NAME_FIELD', 'username')

AUTH1_SESSION_LIMIT = getattr(settings, 'AUTH1_SESSION_LIMIT', 0)

AUTH1_KEY_PREFIX = getattr(settings, 'AUTH1_KEY_PREFIX', 'auth1')

AUTH1_LOGIN_COUNTER = getattr(settings, 'AUTH1_LOGIN_COUNTER', True)
