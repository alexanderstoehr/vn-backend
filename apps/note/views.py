from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response

from apps.note.models import Note
from apps.note.serializer import NoteSerializer
from apps.video.models import Video


# Create your views here.

# # GET all notes from a video
class GetNotesFromVideoView(GenericAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        video_id = self.kwargs.get('video_id')
        return Note.objects.filter(video_id=video_id)

    def get(self, request, *args, **kwargs):
        video_id = self.kwargs.get('video_id')
        try:
            Video.objects.get(id=video_id)
        except Video.DoesNotExist:
            return Response({'error': 'No video with that id'}, status=status.HTTP_404_NOT_FOUND)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# # DELETE an existing note
# # GET single note
# # PATCH an existing single note
class RetrieveUpdateDeleteNoteView(RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()


# # POST a new note
class CreateNoteView(CreateAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def post(self, request, *args, **kwargs):
        video_id = request.data.get('video_id')
        if not video_id:
            return Response({'error': 'Video ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            video = Video.objects.get(id=video_id)
        except Video.DoesNotExist:
            return Response({'error': 'Video not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            note = serializer.save(video=video)
            return Response(NoteSerializer(note).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)