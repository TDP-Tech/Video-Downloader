from django.shortcuts import render
from django.http import HttpResponse
from .forms import YouTubeForm
from .models import YouTubeVideo
from yt_dlp import YoutubeDL

from django.http import StreamingHttpResponse
import os

def download_video(request):
    if request.method == 'POST':
        form = YouTubeForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            quality = form.cleaned_data['quality']
            
            ydl_opts = {
                'format': f'best[height<={quality}]',  # Download best available single file
                'outtmpl': 'downloads/%(title)s.%(ext)s',
            }
            
            with YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                file_path = ydl.prepare_filename(info_dict)
            
                # Save the video information to the database
                video_entry = YouTubeVideo(
                    url=url,
                    title=info_dict.get('title'),
                    download_path=file_path,
                    quality=quality,
                    thumbnail_url=info_dict.get('thumbnail')  # Save the thumbnail URL
                )
                video_entry.save()
            
            def file_iterator(file_name, chunk_size=8192):
                with open(file_name, 'rb') as f:
                    while True:
                        chunk = f.read(chunk_size)
                        if not chunk:
                            break
                        yield chunk

            response = StreamingHttpResponse(file_iterator(file_path), content_type='video/mp4')
            response['Content-Disposition'] = f'attachment; filename="{info_dict.get("title")}.mp4"'
            return response
    else:
        form = YouTubeForm()

    return render(request, 'download.html', {'form': form})
