from django.contrib import admin
from .models import UploadImage


class UploadImageModelAdmin(admin.ModelAdmin):
    list_display = ['image_link', 'upload_at']
    list_display_links = ['image_link', 'upload_at']
    list_filter = ['upload_at']

    class Meta:
        model = UploadImage


admin.site.register(UploadImage, UploadImageModelAdmin)
