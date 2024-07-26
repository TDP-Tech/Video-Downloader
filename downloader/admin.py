from django.contrib import admin
from .models import YouTubeVideo

class YouTubeVideoAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'download_path', 'quality', 'downloaded_at')

admin.site.register(YouTubeVideo, YouTubeVideoAdmin)
