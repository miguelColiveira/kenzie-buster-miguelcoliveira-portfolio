from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        max_length=150,
        validators=[
            UniqueValidator(queryset=User.objects.all(), message="username already taken.")
        ],
    )
    password = serializers.CharField(max_length=150, write_only=True)
    email = serializers.CharField(
        max_length=127,
        validators=[
            UniqueValidator(queryset=User.objects.all(), message="email already registered.")
        ],
    )
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(allow_null=True, default=None)
    is_employee = serializers.BooleanField(allow_null=True, default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict) -> User:
        if validated_data.get("is_employee"):
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password")
        if password:
            instance.set_password(password)
            instance.save()
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, write_only=True)
    password = serializers.CharField(max_length=150, write_only=True)
