from apps.note.models import Note
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "video" ,"note_timestamp", "note_title", "note_description"]