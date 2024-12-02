# apps/tag/urls.py
from django.urls import path
from .views import AttachTagToVideoView, DetachTagFromVideoView

urlpatterns = [
    path('attach-tag/', AttachTagToVideoView.as_view(), name='attach-tag-to-video'),
    path('detach-tag/', DetachTagFromVideoView.as_view(), name='detach-tag-from-video'),

    ]