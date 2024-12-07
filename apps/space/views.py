from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.space.models import Space
from apps.space.serializer import SpaceSerializer, SpaceCreateSerializer


# Create your views here.

# # GET all spaces and its videos from current user
# # POST a new space

class ListCreateSpaceView(ListCreateAPIView):
    serializer_class = SpaceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Space.objects.filter(space_owner__user__id=self.request.user.id)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SpaceCreateSerializer
        return SpaceSerializer

    def post(self, request, *args, **kwargs):
        # Add the video owner to the request data before saving
        data = request.data.copy()
        data['space_owner'] = request.user.id
        serializer = self.get_serializer(data=data)

        # Check if the data is valid and save
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



# # GET a single space and its videos
# # PATCH an existing space
# # DELETE an existing space


class RetrieveUpdateDeleteSpaceView(RetrieveUpdateDestroyAPIView):
    serializer_class = SpaceSerializer
    queryset = Space.objects.all()
    permission_classes = [IsAuthenticated]


    def get_object(self):
        obj = super().get_object()
        if obj.space_owner.user.id != self.request.user.id:
            raise PermissionDenied("You do not have permission to modify this space.")
        return obj
