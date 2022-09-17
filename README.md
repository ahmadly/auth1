# Auth1
This is a simple Django rest library that helps you to have more control over the authentication flow.
- can limit number of sessions
- uses cache as token backend. No model, no migration. and more efficiency and performance
- easy to customize. you can replace your classes everywhere
- handle `prefetch_related` and `select_related` in user loading


### Todo
- [ ] handle jwt as a secondary auth system
- [x] handle USER_SELECT_RELATED and USER_PREFETCH_RELATED on user loading
- [ ] handle SESSION_LIMIT
- [ ] create a pip package + github action + version + auto release
- [x] create default settings 
- [ ] create a simple doc/wiki


### sample settings.py

```python

AUTH1_VIEWS_LOGIN = 'auth1.views.LoginView'
AUTH1_VIEWS_LOGOUT = 'auth1.views.LogoutView'
AUTH1_VIEWS_VERIFY = 'auth1.views.VerifyView'
AUTH1_VIEWS_REFRESH = 'auth1.views.RefreshView'
AUTH1_VIEWS_REGISTER = 'auth1.views.RegisterView'
AUTH1_VIEWS_CONFIRM = 'auth1.views.ConfirmView'
AUTH1_VIEWS_BLOCK = 'auth1.views.BlockView'
AUTH1_VIEWS_PROFILE = 'auth1.views.ProfileView'

AUTH1_SERIALIZERS_LOGIN = 'auth1.serializers.LoginSerializer'
AUTH1_SERIALIZERS_LOGOUT = 'auth1.serializers.LogoutSerializer'
AUTH1_SERIALIZERS_VERIFY = 'auth1.serializers.VerifySerializer'
AUTH1_SERIALIZERS_REFRESH = 'auth1.serializers.RefreshSerializer'
AUTH1_SERIALIZERS_REGISTER = 'auth1.serializers.RegisterSerializer'
AUTH1_SERIALIZERS_CONFIRM = 'auth1.serializers.ConfirmSerializer'
AUTH1_SERIALIZERS_BLOCK = 'auth1.serializers.BlockSerializer'
AUTH1_SERIALIZERS_PROFILE = 'auth1.serializers.ProfileSerializer'

AUTH1_TOKEN_CACHE_ALIAS = 'default'
AUTH1_TOKEN = 'auth1.tokens.SimpleToken'
AUTH1_ACCESS_TOKEN_EXPIRATION = 1 * 60 * 60
AUTH1_REFRESH_TOKEN_EXPIRATION = 24 * 60 * 60
AUTH1_USER_SELECT_RELATED = []
AUTH1_USER_PREFETCH_RELATED = []
AUTH1_USER_ID_FIELD = 'id'
AUTH1_USER_NAME_FIELD = 'username'
AUTH1_SESSION_LIMIT = 0
AUTH1_KEY_PREFIX = 'auth1'

```
