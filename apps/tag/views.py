# apps/tag/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tag
from .serializer import TagSerializer
from apps.video.models import Video  # Import the Video model

class AttachTagToVideoView(APIView):
    def post(self, request, *args, **kwargs):
        tag_name = request.data.get('tag_name')
        video_id = self.kwargs.get('video_id')

        if not tag_name or not video_id:
            return Response({'error': 'Tag name and video_id are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            video = Video.objects.get(id=video_id)
        except Video.DoesNotExist:
            return Response({'error': 'Video not found'}, status=status.HTTP_404_NOT_FOUND)

        tag, created = Tag.objects.get_or_create(tag_name=tag_name)
        video.tags.add(tag)
        video.save()

        serializer = TagSerializer(tag)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

class DetachTagFromVideoView(APIView):
    def post(self, request, *args, **kwargs):
        tag_name = request.data.get('tag_name')
        video_id = self.kwargs.get('video_id')

        if not tag_name or not video_id:
            return Response({'error': 'Tag name and video_id are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            video = Video.objects.get(id=video_id)
        except Video.DoesNotExist:
            return Response({'error': 'Video not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            tag = Tag.objects.get(tag_name=tag_name)
        except Tag.DoesNotExist:
            return Response({'error': 'Tag not found'}, status=status.HTTP_404_NOT_FOUND)

        video.tags.remove(tag)
        video.save()

        return Response({'message': 'Tag removed from video'}, status=status.HTTP_200_OK)