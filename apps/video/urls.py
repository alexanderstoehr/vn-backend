from django.urls import path

from apps.video.views import RetrieveUpdateDeletevideoView, ListCreateVideosView

urlpatterns = [
    path("video/", ListCreateVideosView.as_view(), name='post-video'),
    path("video/<pk>/", RetrieveUpdateDeletevideoView.as_view(), name='get-patch-delete-video'),
    ]