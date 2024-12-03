from django.urls import path

from apps.category.views import ListAllCategories, AttachCategoryToVideo

urlpatterns = [
    path('', ListAllCategories.as_view(), name='list-all-categories'),
    path("attach/<int:video_id>/", AttachCategoryToVideo.as_view(), name="attach-category-to-video"),
]
