from django import forms

class YouTubeForm(forms.Form):
    url = forms.URLField(label='YouTube URL or Playlist URL', max_length=200)
    quality = forms.ChoiceField(label='Quality', choices=[
        ('360p', '360p'),
        ('480p', '480p'),
        ('720p', '720p'),
        ('1080p', '1080p'),
    ])
