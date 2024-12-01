from django.db import models

from apps.space.models import Space


# Create your models here.
class Video(models.Model):

    space = models.ForeignKey(Space, on_delete=models.CASCADE, related_name='videos')
    # notes
    # tags
    # category

    video_title = models.CharField(max_length=100)
    video_description = models.TextField(max_length=500, blank=True, null=True)

    video_host_url = models.CharField(max_length=200)
    video_host_id = models.CharField(max_length=100)
    video_host_thumbnail_url = models.CharField(max_length=200)

    is_public = models.BooleanField(default=False)
    is_shareable = models.BooleanField(default=False)
    is_shareable_to_all = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title