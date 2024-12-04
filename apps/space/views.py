from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.space.models import Space
from apps.space.serializer import SpaceSerializer


# Create your views here.

# # GET all spaces and its videos from current user
# # POST a new space

class ListCreateSpaceView(ListCreateAPIView):
    serializer_class = SpaceSerializer
    queryset = Space.objects.all()


# # GET a single space and its videos
# # PATCH an existing space
# # DELETE an existing space


class RetrieveUpdateDeleteSpaceView(RetrieveUpdateDestroyAPIView):
    serializer_class = SpaceSerializer
    queryset = Space.objects.all()
