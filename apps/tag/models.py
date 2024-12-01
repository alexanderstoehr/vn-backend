from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=255)
    video = models.ManyToManyField('video.Video', related_name='tags')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name