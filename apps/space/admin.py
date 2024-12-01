from django.contrib import admin

from apps.space.models import Space


# Register your models here.
@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Space._meta.fields]
    search_fields = ['space_name', 'id']
    list_filter = ['space_name', 'id']