from rest_framework import serializers
from .models import Space
from ..user_profile.serializer import UserProfileSerializer
from ..video.serializer import VideoSerializer


class SpaceSerializer(serializers.ModelSerializer):
    space_owner = UserProfileSerializer()
    videos = VideoSerializer(many=True, read_only=True)
    videos_count = serializers.SerializerMethodField()

    class Meta:
        model = Space
        fields = ['id', 'space_name', 'space_description', 'space_owner',"videos_count", "videos"]

    def get_videos_count(self, obj):
        return obj.videos.count()

class SpaceCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Space
        fields = ["space_name", "space_description","space_owner"]

        extra_kwargs = {
            "space_name": {"required": True},
            "space_description": {"required": True},
            "space_owner": {"required": True},
            }
