from django.urls import path

from apps.space.views import ListCreateSpaceView, RetrieveUpdateDeleteSpaceView

urlpatterns = [
    path("space/", ListCreateSpaceView.as_view(), name='List Spaces'),
    path("space/<pk>/", RetrieveUpdateDeleteSpaceView.as_view(), name='Edit Space'),

    ]