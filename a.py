a = dict(

    AUTH1_VIEWS={
        'LOGIN': 'auth1.views.LoginView',
        'LOGOUT': 'auth1.views.LogoutView',
        'VERIFY': 'auth1.views.VerifyView',
        'REFRESH': 'auth1.views.RefreshView',
        'REGISTER': 'auth1.views.RegisterView',
        'CONFIRM': 'auth1.views.ConfirmView',
        'BLOCK': 'auth1.views.BlockView',
    },

    AUTH1_SERIALIZERS={
        'LOGIN': 'auth1.serializers.LoginSerializer',
        'LOGOUT': 'auth1.serializers.LogoutSerializer',
        'VERIFY': 'auth1.serializers.VerifySerializer',
        'REFRESH': 'auth1.serializers.RefreshSerializer',
        'REGISTER': 'auth1.serializers.RegisterSerializer',
        'CONFIRM': 'auth1.serializers.ConfirmSerializer',
        'BLOCK': 'auth1.serializers.BlockSerializer',
    },

    AUTH1_TOKEN_CACHE_ALIAS='default',
    AUTH1_TOKEN='auth1.tokens.SimpleToken',
    AUTH1_ACCESS_TOKEN_EXPIRATION=1 * 60 * 60,  # 1 hour
    AUTH1_REFRESH_TOKEN_EXPIRATION=24 * 60 * 60,  # 24 hours
    AUTH1_USER_SELECT_RELATED=None,
    AUTH1_USER_PREFETCH_RELATED=None,
    AUTH1_USER_ID_FIELD='id',
    AUTH1_USER_NAME_FIELD='username',
    AUTH1_SESSION_LIMIT=0,  # 0 means no limit
    AUTH1_KEY_PREFIX='auth1',

)


print(a)