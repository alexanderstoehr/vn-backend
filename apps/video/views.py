from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.space.models import Space
from apps.video.models import Video
from apps.video.serializer import VideoSerializer


# Create your views here.

# # GET all videos from a space
class ListCreateVideosView(ListCreateAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# # GET a single video and its notes, tags and categories -- by space
# # PATCH a single existing video
# # DELETE a single existing video
class RetrieveUpdateDeletevideoView(RetrieveUpdateDestroyAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


# # POST a new video with tags and categories
