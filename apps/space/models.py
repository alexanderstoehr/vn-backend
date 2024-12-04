from django.db import models

from apps.user_profile.models import UserProfile


# Create your models here.
class Space(models.Model):
    space_owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='spaces')
    #videos
    space_name = models.CharField(max_length=100)
    space_description = models.TextField(max_length=500, blank=True, null=True)
    is_public = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.space_name
