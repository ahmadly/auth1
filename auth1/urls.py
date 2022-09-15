from django.conf import settings
from django.urls import path
from django.utils.module_loading import import_string

LoginView = import_string(settings.REST_FRAMEWORK['DEFAULT_VIEW_CLASSES']['LOGIN'])
LogoutView = import_string(settings.REST_FRAMEWORK['DEFAULT_VIEW_CLASSES']['LOGOUT'])
VerifyView = import_string(settings.REST_FRAMEWORK['DEFAULT_VIEW_CLASSES']['VERIFY'])
RefreshView = import_string(settings.REST_FRAMEWORK['DEFAULT_VIEW_CLASSES']['REFRESH'])
RegisterView = import_string(settings.REST_FRAMEWORK['DEFAULT_VIEW_CLASSES']['REGISTER'])
ConfirmView = import_string(settings.REST_FRAMEWORK['DEFAULT_VIEW_CLASSES']['CONFIRM'])
BlockView = import_string(settings.REST_FRAMEWORK['DEFAULT_VIEW_CLASSES']['BLOCK'])

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('verify/', VerifyView.as_view(), name='logout'),
    path('refresh/', RefreshView.as_view(), name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm/', ConfirmView.as_view(), name='confirm'),
    path('block/', BlockView.as_view(), name='block'),
]
