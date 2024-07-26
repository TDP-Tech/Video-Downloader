from django.db import models

class YouTubeVideo(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=200)
    download_path = models.CharField(max_length=200)
    quality = models.CharField(max_length=50)
    downloaded_at = models.DateTimeField(auto_now_add=True)
    thumbnail_url = models.URLField(max_length=200, blank=True, null=True)  # New field for thumbnail URL

    def __str__(self):
        return self.title
