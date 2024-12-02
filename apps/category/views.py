from unicodedata import category

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.category.models import Category
from apps.category.serializer import CategorySerializer
from apps.video.models import Video


# Create your views here.

# # GET all the categories read only
class ListAllCategories (ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AttachCategoryToVideo(APIView):
    def post(self, request, *args, **kwargs):
        category_id = request.data.get('category_id')
        video_id = request.data.get('video_id')

        if not category_id or not video_id:
            return Response({'error': 'Category ID and video ID are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            video = Video.objects.get(id=video_id)
        except Video.DoesNotExist:
            return Response({'error': 'Video not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

        video.category = category
        video.save()

        return Response({'message': 'Category attached to video'}, status=status.HTTP_200_OK)