from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        exclude = ['publish_date','author',]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)