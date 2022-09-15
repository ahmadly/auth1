from rest_framework import fields


class UsernameField(fields.CharField):
    def __init__(self, **kwargs):
        kwargs['max_length'] = 256
        kwargs['min_length'] = 1
        kwargs['allow_null'] = False
        kwargs['write_only'] = True
        super().__init__(**kwargs)


class PasswordField(fields.CharField):
    def __init__(self, **kwargs):
        kwargs['max_length'] = 256
        kwargs['min_length'] = 1
        kwargs['allow_null'] = False
        kwargs['write_only'] = True
        super().__init__(**kwargs)


class AccessTokenField(fields.CharField):
    default_validators = []  # TODO: use token class validators

    def __init__(self, **kwargs):
        kwargs['max_length'] = 256
        kwargs['min_length'] = 1
        kwargs['allow_null'] = False
        kwargs['write_only'] = True
        super().__init__(**kwargs)


class RefreshTokenField(fields.CharField):
    def __init__(self, **kwargs):
        kwargs['max_length'] = 256
        kwargs['min_length'] = 1
        kwargs['allow_null'] = False
        kwargs['write_only'] = True
        super().__init__(**kwargs)
