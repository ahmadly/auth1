from django.conf import settings
from rest_framework import status, response, views, permissions

from django.utils.module_loading import import_string

LoginSerializer = import_string(settings.REST_FRAMEWORK['DEFAULT_SERIALIZER_CLASSES']['LOGIN'])
LogoutSerializer = import_string(settings.REST_FRAMEWORK['DEFAULT_SERIALIZER_CLASSES']['LOGOUT'])
RegisterSerializer = import_string(settings.REST_FRAMEWORK['DEFAULT_SERIALIZER_CLASSES']['REGISTER'])
ConfirmSerializer = import_string(settings.REST_FRAMEWORK['DEFAULT_SERIALIZER_CLASSES']['CONFIRM'])
VerifySerializer = import_string(settings.REST_FRAMEWORK['DEFAULT_SERIALIZER_CLASSES']['VERIFY'])
RefreshSerializer = import_string(settings.REST_FRAMEWORK['DEFAULT_SERIALIZER_CLASSES']['REFRESH'])


class LoginView(views.APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return response.Response(serializer.validated_data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, **kwargs):
        serializer = LogoutSerializer(data=request.data)
        if serializer.is_valid():
            return response.Response(serializer.validated_data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, **kwargs):
        serializer = VerifySerializer(data=request.data)
        if serializer.is_valid():
            return response.Response(serializer.validated_data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RefreshView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, **kwargs):
        serializer = RefreshSerializer(data=request.data)
        if serializer.is_valid():
            return response.Response(serializer.validated_data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(views.APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            return response.Response(serializer.validated_data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmView(views.APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, **kwargs):
        serializer = ConfirmSerializer(data=request.data)
        if serializer.is_valid():
            return response.Response(serializer.validated_data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
