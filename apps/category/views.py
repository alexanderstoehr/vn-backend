from django.shortcuts import render
from rest_framework.generics import ListAPIView

from apps.category.models import Category
from apps.category.serializer import CategorySerializer


# Create your views here.

# # GET all the categories read only
class ListAllCategories (ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer