from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.space.models import Space
from apps.space.serializer import SpaceSerializer


# Create your views here.

# # GET all spaces and its videos from current user
# # POST a new space

class ListCreateSpaceView(ListCreateAPIView):
    serializer_class = SpaceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Space.objects.filter(space_owner__user=self.request.user)


# # GET a single space and its videos
# # PATCH an existing space
# # DELETE an existing space


class RetrieveUpdateDeleteSpaceView(RetrieveUpdateDestroyAPIView):
    serializer_class = SpaceSerializer
    queryset = Space.objects.all()
