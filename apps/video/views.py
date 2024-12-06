from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.video.models import Video
from apps.video.serializer import VideoSerializer, VideoCreateSerializer


# Create your views here.

# # GET all videos from a space
class ListCreateVideosView(ListCreateAPIView):
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]
    #queryset = Video.objects.all()

    def get_queryset(self):
        return Video.objects.filter(video_owner__user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return VideoCreateSerializer
        return VideoSerializer


    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Add the video owner to the request data before saving
        data = request.data.copy()
        data['video_owner'] = request.user.id
        serializer = self.get_serializer(data=data)

        # Check if the data is valid and save
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# # GET a single video and its notes, tags and categories -- by space
# # PATCH a single existing video
# # DELETE a single existing video
class RetrieveUpdateDeletevideoView(RetrieveUpdateDestroyAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

    def get_object(self):
        obj = super().get_object()
        if obj.video_owner.user.id != self.request.user.id:
            raise PermissionDenied("You do not have permission to modify this Video.")
        return obj


# # POST a new video with tags and categories
