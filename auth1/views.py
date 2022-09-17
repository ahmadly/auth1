from django.utils.module_loading import import_string
from rest_framework import permissions, response, status, views

from .settings import (
    AUTH1_SERIALIZERS_BLOCK,
    AUTH1_SERIALIZERS_CONFIRM,
    AUTH1_SERIALIZERS_LOGIN,
    AUTH1_SERIALIZERS_LOGOUT,
    AUTH1_SERIALIZERS_PROFILE,
    AUTH1_SERIALIZERS_REFRESH,
    AUTH1_SERIALIZERS_REGISTER,
    AUTH1_SERIALIZERS_VERIFY
)

LoginSerializer = import_string(AUTH1_SERIALIZERS_LOGIN)
LogoutSerializer = import_string(AUTH1_SERIALIZERS_LOGOUT)
RegisterSerializer = import_string(AUTH1_SERIALIZERS_REGISTER)
ConfirmSerializer = import_string(AUTH1_SERIALIZERS_CONFIRM)
VerifySerializer = import_string(AUTH1_SERIALIZERS_VERIFY)
RefreshSerializer = import_string(AUTH1_SERIALIZERS_REFRESH)
BlockSerializer = import_string(AUTH1_SERIALIZERS_BLOCK)
ProfileSerializer = import_string(AUTH1_SERIALIZERS_PROFILE)


class LoginView(views.APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, **kwargs):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return response.Response(serializer.validated_data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, **kwargs):
        serializer = LogoutSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return response.Response(serializer.validated_data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, **kwargs):
        serializer = VerifySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return response.Response(serializer.validated_data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RefreshView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, **kwargs):
        serializer = RefreshSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return response.Response(serializer.validated_data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(views.APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, **kwargs):
        serializer = RegisterSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return response.Response(serializer.validated_data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmView(views.APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, **kwargs):
        serializer = ConfirmSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return response.Response(serializer.validated_data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlockView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, **kwargs):
        serializer = BlockSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return response.Response(serializer.validated_data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, **kwargs):
        serializer = ProfileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return response.Response(serializer.validated_data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
