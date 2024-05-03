from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """Serializer for User model."""

    class Meta:
        model = User
        fields = ["id", "password", "email", "phone", "city"]
        extra_kwargs = {"password": {"write_only": True}}
