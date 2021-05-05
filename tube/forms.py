from django import forms
from .models import Video,VideoComment

class VideoForm(forms.ModelForm):
    class Meta:
        model  = Video
        fields = ["title", "description", "image", "movie", "category", "tag",]

class VideoEditForm(forms.ModelForm):
    class Meta:
        model  = Video
        fields = ["title", "description", "dt",]

class VideoCommentForm(forms.ModelForm):
    class Meta:
        model  = VideoComment
        fields = [ "content", "target", ] #←フォームにないdtがあると常にバリデーションエラーになってしまう。

"""
class VideoCommentForm(forms.ModelForm):
    class Meta:
        model  = VideoComment
        fields = ["content", "target", "dt",]

    class Meta2:
        model  = Video
        fields = ["title", "description", "image", "movie", "category", "tag", ]
"""
