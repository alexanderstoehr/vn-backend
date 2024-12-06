# apps/tag/urls.py
from django.urls import path
from .views import AttachTagToVideoView, DetachTagFromVideoView, ListUsersTagsView

urlpatterns = [
    path('tag/attach/<int:video_id>/', AttachTagToVideoView.as_view(), name='attach-tag-to-video'),
    path('tag/detach/<int:video_id>/', DetachTagFromVideoView.as_view(), name='detach-tag-from-video'),
    path('tag/user/', ListUsersTagsView.as_view(), name='list-users-tags'),
    ]