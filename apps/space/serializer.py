from rest_framework import serializers
from .models import Space
from ..user_profile.serializer import UserProfileSerializer
from ..video.serializer import VideoSerializer


class SpaceSerializer(serializers.ModelSerializer):
    space_owner = UserProfileSerializer()
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Space
        fields = ['id', 'space_name', 'space_description', 'space_owner', "videos"]

