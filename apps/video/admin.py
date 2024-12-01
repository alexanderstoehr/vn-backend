from django.contrib import admin

from apps.video.models import Video


# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Video._meta.fields]