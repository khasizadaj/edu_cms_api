from django.contrib.auth.models import Group, Permission, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="users-detail")

    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]
        extra_exclude = ("user_permissions",)
        lookup_field = "username"


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="groups-detail")

    class Meta:
        model = Group
        fields = ["url", "name"]
        lookup_field = "name"


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="permissions-detail")

    class Meta:
        model = Permission
        fields = ["url", "name"]
