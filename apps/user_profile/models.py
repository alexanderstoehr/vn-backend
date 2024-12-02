from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model() # get the current user model

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    external_user_id = models.CharField(max_length=100, blank=True, null=True)

    is_following = models.ManyToManyField('self', symmetrical=False, related_name='followed_by', blank=True)
    about_me = models.TextField(blank=True, null=True, max_length=1500)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email}'s profile"