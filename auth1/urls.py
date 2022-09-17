from django.conf import settings
from django.urls import path
from django.utils.module_loading import import_string

from .settings import (
    AUTH1_VIEWS_BLOCK,
    AUTH1_VIEWS_CONFIRM,
    AUTH1_VIEWS_LOGIN,
    AUTH1_VIEWS_LOGOUT,
    AUTH1_VIEWS_REFRESH,
    AUTH1_VIEWS_REGISTER,
    AUTH1_VIEWS_VERIFY,
    AUTH1_VIEWS_PROFILE,
)

LoginView = import_string(AUTH1_VIEWS_LOGIN)
LogoutView = import_string(AUTH1_VIEWS_LOGOUT)
VerifyView = import_string(AUTH1_VIEWS_VERIFY)
RefreshView = import_string(AUTH1_VIEWS_REFRESH)
RegisterView = import_string(AUTH1_VIEWS_REGISTER)
ConfirmView = import_string(AUTH1_VIEWS_CONFIRM)
BlockView = import_string(AUTH1_VIEWS_BLOCK)
ProfileView = import_string(AUTH1_VIEWS_PROFILE)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('verify/', VerifyView.as_view(), name='logout'),
    path('refresh/', RefreshView.as_view(), name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm/', ConfirmView.as_view(), name='confirm'),
    path('block/', BlockView.as_view(), name='block'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
