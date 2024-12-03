from django.urls import path

from apps.note.views import GetNotesFromVideoView, RetrieveUpdateDeleteNoteView, CreateNoteView

urlpatterns = [
    path("notes/<int:video_id>/", GetNotesFromVideoView.as_view(), name='get-notes-from-video'),
    path("note/<int:video_id>", CreateNoteView.as_view(), name='Create note'),
    path("note/<pk>/", RetrieveUpdateDeleteNoteView.as_view(), name='Edit note'),
]