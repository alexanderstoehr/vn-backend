# authentication/urls.py
from django.urls import path
from .views import SyncUserView

urlpatterns = [
    path('user/', SyncUserView.as_view(), name='sync-user'),
]