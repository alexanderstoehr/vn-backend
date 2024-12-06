from rest_framework import serializers
from apps.user_profile.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ["id", "external_user_id"]

class UserProfileVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = [ "id", "external_user_id"]