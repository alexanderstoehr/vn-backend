from django.db import models

from apps.video.models import Video


# Create your models here.
class Note(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='notes')

    note_timestamp = models.CharField(max_length=100)
    note_title = models.CharField(max_length=100)
    note_description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.note_title