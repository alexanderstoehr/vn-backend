from django.urls import path

from apps.category.views import ListAllCategories

urlpatterns = [
    path('', ListAllCategories.as_view(), name='list-all-categories'),
]
