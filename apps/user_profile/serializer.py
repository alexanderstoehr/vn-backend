from rest_framework import serializers
from apps.user_profile.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = UserProfile
        fields = ["user", "external_user_id", "about_me"]

class UserProfileVideoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = UserProfile
        fields = ["user", "id", "external_user_id"]