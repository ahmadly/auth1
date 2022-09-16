# Auth1
This is a simple Django rest library that helps you to have more control over the authentication flow.
- can limit number of sessions
- uses cache as token backend. No model, no migration. and more efficiency and performance
- easy to customize. you can replace your classes everywhere
- handle `prefetch_related` and `select_related` in user loading


### Todo
- [ ] handle jwt as a secondary auth system
- [ ] handle USER_SELECT_RELATED and USER_PREFETCH_RELATED on user loading
- [ ] handle SESSION_LIMIT
- [ ] create a pip package + github action + version + auto release
- [ ] create default settings 
- [ ] create a simple doc/wiki


### sample settings.py

```python

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'auth1.authentications.TokenAuthentication',
    ],
    'DEFAULT_VIEW_CLASSES': {
        'LOGIN': 'auth1.views.LoginView',
        'LOGOUT': 'auth1.views.LogoutView',
        'VERIFY': 'auth1.views.VerifyView',
        'REFRESH': 'auth1.views.RefreshView',
        'REGISTER': 'auth1.views.RegisterView',
        'CONFIRM': 'auth1.views.ConfirmView',
        'BLOCK': 'auth1.views.BlockView',
    },
    'DEFAULT_SERIALIZER_CLASSES': {
        'LOGIN': 'auth1.serializers.LoginSerializer',
        'LOGOUT': 'auth1.serializers.LogoutSerializer',
        'VERIFY': 'auth1.serializers.VerifySerializer',
        'REFRESH': 'auth1.serializers.RefreshSerializer',
        'REGISTER': 'auth1.serializers.RegisterSerializer',
        'CONFIRM': 'auth1.serializers.ConfirmSerializer',
        'BLOCK': 'auth1.serializers.BlockSerializer',
    },

    'TOKEN_CACHE_ALIAS': 'default',
    'TOKEN_CLASS': 'auth1.tokens.SimpleToken',
    'ACCESS_TOKEN_EXPIRATION': 1 * 60 * 60,  # 1 hour
    'REFRESH_TOKEN_EXPIRATION': 24 * 60 * 60,  # 24 hours
    'USER_SELECT_RELATED': None,
    'USER_PREFETCH_RELATED': None,
    'USER_ID_FIELD': 'id',
    'SESSION_LIMIT': 1,
    'DEFAULT_KEY_PREFIX': 'auth1',
}
```
