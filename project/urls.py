"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt import views as jwt_views


# Schema view for API documentation
schema_view = get_schema_view(
   openapi.Info(
      title="Veenotes API",
      default_version='v1',
      description="Veenotes API provides endpoints to manage users, videos, bookmarks, and collections, enabling a seamless and interactive learning experience.",
      terms_of_service="https://veenotes.com/terms/",
      contact=openapi.Contact(email="hello@veenotes.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True, # Set to False restrict access to protected endpoints
   permission_classes=(permissions.AllowAny,), # Permissions for docs access
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("categories/", include("apps.category.urls")), # Include the Category app URLs
    path('', include('apps.tag.urls')),  # Include the Tag app URLs
    path('', include('apps.note.urls')),  # Include the Note app URLs
    path('', include('apps.video.urls')),  # Include the Video app URLs
    path('', include('apps.space.urls')),  # Include the Space app URLs
    path('auth/', include('apps.registration.urls')),

]

