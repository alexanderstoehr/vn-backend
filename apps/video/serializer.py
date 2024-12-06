from apps.category.serializer import CategorySerializer
from apps.note.serializer import NoteSerializer
from apps.tag.serializer import TagSerializer
from apps.user_profile.serializer import UserProfileSerializer, UserProfileVideoSerializer
from apps.video.models import Video
from rest_framework import serializers


class VideoSerializer(serializers.ModelSerializer):
    video_owner = UserProfileVideoSerializer()
    #notes = NoteSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    category = CategorySerializer()
    notes_count = serializers.SerializerMethodField()
    tags_count = serializers.SerializerMethodField()


    class Meta:
        model = Video
        fields = ["id", "video_title", "video_description","video_host_url", "video_host_id","video_host_thumbnail_url","created_at","video_owner", "notes_count", "category","tags_count", "tags"]


    def get_notes_count(self, obj):
        return obj.notes.count()

    def get_tags_count(self, obj):
        return obj.tags.count()

class VideoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ["space", "video_title", "video_description","video_host_url", "video_host_id","video_host_thumbnail_url","video_owner", "category",]

        extra_kwargs = {
            "space": {"required": True},
            "video_title": {"required": True},
            "video_title": {"required": True},
            "video_description": {"required": True},
            "video_host_url": {"required": True},
            "video_host_id": {"required": True},
            "video_host_thumbnail_url": {"required": True},
            "category": {"required": True},
            }