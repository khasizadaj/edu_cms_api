from django.contrib.auth.models import Group, Permission, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="users-detail")

    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]
        extra_exclude = ("user_permissions",)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="groups-detail")

    class Meta:
        model = Group
        fields = ["url", "name"]


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="permissions-detail")

    class Meta:
        model = Permission
        fields = ["url", "name"]


class UserSerializerFromScratch(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=150, required=False)
    last_name = serializers.CharField(max_length=150, required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True)
    last_login = serializers.DateTimeField(read_only=True, format="%H:%M %d-%m-%y")

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        instance.username = validated_data.get("username", instance.username)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        instance.last_login = validated_data.get("last_login", instance.last_login)

        if "password" in validated_data.keys():
            instance.set_password(validated_data["password"])

        instance.save()
        return instance


class UserSerializerFromModel(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "last_login"]
