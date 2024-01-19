from rest_framework import authentication, viewsets, permissions
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth.models import Group, Permission, User
from .serializers import (
    UserSerializerFromModel,
    UserSerializerFromScratch,
    GroupSerializer,
    PermissionSerializer,
    UserSerializer,
)


class UsersListFromScratch(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]

    def get(self, request: Request) -> Response:
        queryset = User.objects.all()
        serializer = UserSerializerFromScratch(queryset, many=True)
        return Response(serializer.data)


class UsersListFromModel(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]

    def get(self, request: Request) -> Response:
        queryset = User.objects.all()
        serializer = UserSerializerFromModel(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAuthenticated]
