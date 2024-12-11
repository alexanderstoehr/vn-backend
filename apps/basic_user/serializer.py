from rest_framework import serializers

from apps.basic_user.admin import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            }
